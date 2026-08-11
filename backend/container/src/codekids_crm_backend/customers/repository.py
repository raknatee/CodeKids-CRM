from datetime import datetime, timezone

from pymongo.collection import Collection
from pymongo.database import Database

from codekids_crm_backend.customers.schemas import (
    CustomerCreate,
    CustomerOut,
    CustomerReplace,
)

COLLECTION_NAME = "customers"
COUNTER_ID = "customer_uid"


class CustomerNotFoundError(Exception):
    pass


class CustomerRepository:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._collection: Collection = db[COLLECTION_NAME]

    def _next_uid(self) -> str:
        """
        Gen uid แบบ auto-increment โดยใช้ collection `counters` เป็นตัวนับกลาง
        ใช้ find_one_and_update แบบ atomic กัน race condition ตอนสร้างพร้อมกันหลาย request
        """
        result = self._db["counters"].find_one_and_update(
            {"_id": COUNTER_ID},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=True,
        )
        if not result:
            raise RuntimeError("Failed to generate or retrieve counter for UID")
        return str(result["seq"])

    def create(self, payload: CustomerCreate) -> CustomerOut:
        now = datetime.now(timezone.utc)
        doc = CustomerOut(
            uid=self._next_uid(),
            updated_at=now,
            **payload.model_dump(),
        )
        self._collection.insert_one(doc.model_dump())
        return doc

    def get_by_uid(self, uid: str) -> CustomerOut:
        doc = self._collection.find_one({"uid": uid})
        if doc is None:
            raise CustomerNotFoundError(f"customer uid={uid} not found")
        return CustomerOut.model_validate(doc)

    def list(
        self,
        skip: int = 0,
        limit: int = 20,
        search: str | None = None,
    ) -> tuple[int, list[CustomerOut]]:
        """List พร้อม pagination และ search แบบง่าย (ชื่อ/นามสกุล/นามแฝง/เบอร์/อีเมล/codekids_id)"""
        query: dict = {}
        if search:
            regex = {"$regex": search, "$options": "i"}
            query["$or"] = [
                {"first_name": regex},
                {"last_name": regex},
                {"nickname": regex},
                {"phone": regex},
                {"email": regex},
                {"codekids_id": regex},
            ]

        total = self._collection.count_documents(query)
        cursor = self._collection.find(query).skip(skip).limit(limit).sort("uid", 1)
        return total, [CustomerOut.model_validate(doc) for doc in cursor]

    def replace(self, uid: str, payload: CustomerReplace) -> CustomerOut:
        """ใช้กับ PUT — แทนที่ทุก field ที่แก้ไขได้ทั้งก้อน (ยกเว้น uid เดิม)"""
        update_fields = payload.model_dump()
        update_fields["updated_at"] = datetime.now(timezone.utc)

        doc = self._collection.find_one_and_update(
            {"uid": uid},
            {"$set": update_fields},
            return_document=True,
        )
        if doc is None:
            raise CustomerNotFoundError(f"customer uid={uid} not found")
        return CustomerOut.model_validate(doc)

    def delete(self, uid: str) -> None:
        result = self._collection.delete_one({"uid": uid})
        if result.deleted_count == 0:
            raise CustomerNotFoundError(f"customer uid={uid} not found")