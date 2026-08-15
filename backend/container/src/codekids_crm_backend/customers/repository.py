from datetime import datetime, timezone
import uuid

from pymongo.collection import Collection
from pymongo.database import Database

from codekids_crm_backend.customers.models import LeadStatus
from codekids_crm_backend.customers.schemas import (
    CustomerCreate,
    CustomerOut,
    CustomerReplace,
)

COLLECTION_NAME = "customers"
_EXCLUDE_ID = {"_id": 0} #ทิ้ง _id ของ mongo ไม่ส่งไปกับ response


class CustomerNotFoundError(Exception):
    pass


class CustomerRepository:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._collection: Collection = db[COLLECTION_NAME]

    def create(self, payload: CustomerCreate) -> CustomerOut:
        now = datetime.now(timezone.utc)
        doc: CustomerOut = {
            "lead_status": LeadStatus.NEW_LEAD,
            **payload,
            "uid": str(uuid.uuid4()),
            "updated_at": now,
        }
        self._collection.insert_one(dict(doc))
        return doc

    def get_by_uid(self, uid: str) -> CustomerOut:
        doc = self._collection.find_one({"uid": uid}, projection=_EXCLUDE_ID)
        if doc is None:
            raise CustomerNotFoundError(f"customer uid={uid} not found")
        return doc

    def list(
        self,
        skip: int = 0,
        limit: int = 20,
        search: str | None = None,) -> tuple[int, list[CustomerOut]]:
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
        cursor = (
            self._collection.find(query, projection=_EXCLUDE_ID)
            .skip(skip)
            .limit(limit)
            .sort("uid", 1)
        )
        return total, list(cursor)

    def replace(self, uid: str, payload: CustomerReplace) -> CustomerOut:
        update_fields: dict = {**payload, "update_at": datetime.now(timezone.utc)}

        doc = self._collection.find_one_and_update(
            {"uid": uid},
            {"$set": update_fields},
            projection=_EXCLUDE_ID,
            return_document=True,
        )
        if doc is None:
            raise CustomerNotFoundError(f"customer uid={uid} not found")
        return doc

    def delete(self, uid: str) -> None:
        result = self._collection.delete_one({"uid": uid})
        if result.deleted_count == 0:
            raise CustomerNotFoundError(f"customer uid={uid} not found")