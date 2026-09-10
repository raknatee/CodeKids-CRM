from datetime import datetime, timezone
import uuid

from pymongo.collection import Collection
from pymongo.database import Database

from codekids_crm_backend.contact_sessions.schemas import (
    ContactSessionCreate,
    ContactSessionOut,
    ContactSessionReplace,
)

COLLECTION_NAME = "contact_sessions"
_EXCLUDE_ID = {"_id": 0}  # ทิ้ง _id ของ mongo ไม่ส่งไปกับ response

class ContactSessionNotFoundError(Exception):
    pass

class ContactSessionRepository:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._collection: Collection = db[COLLECTION_NAME]

    def create(self, payload: ContactSessionCreate) -> ContactSessionOut:
        now = datetime.now(timezone.utc)
        doc: ContactSessionOut = {
            **payload,
            "session_id": str(uuid.uuid4()),
            "updated_at": now,
        }
        self._collection.insert_one(dict(doc))
        return doc

    def get_by_session_id(self, session_id: str) -> ContactSessionOut:
        doc = self._collection.find_one(
            {"session_id": session_id}, projection=_EXCLUDE_ID
        )
        if doc is None:
            raise ContactSessionNotFoundError(
                f"contact session session_id={session_id} not found"
            )
        return doc

    def replace(
        self, session_id: str, payload: ContactSessionReplace
    ) -> ContactSessionOut:
        update_fields: dict = {**payload, "updated_at": datetime.now(timezone.utc)}

        doc = self._collection.find_one_and_update(
            {"session_id": session_id},
            {"$set": update_fields},
            projection=_EXCLUDE_ID,
            return_document=True,
        )
        if doc is None:
            raise ContactSessionNotFoundError(
                f"contact session session_id={session_id} not found"
            )
        return doc

    def delete(self, session_id: str) -> None:
        result = self._collection.delete_one({"session_id": session_id})
        if result.deleted_count == 0:
            raise ContactSessionNotFoundError(
                f"contact session session_id={session_id} not found"
            )

    def list(
        self,
        skip: int = 0,
        limit: int = 20,
        internal_id: str | None = None,
    ) -> tuple[int, list[ContactSessionOut]]:
        """Pagination list กรองด้วย internal_id (ดึง ticket log ทั้งหมดของลูกค้าคนนั้น)"""
        query: dict = {}
        if internal_id:
            query["internal_id"] = internal_id

        total = self._collection.count_documents(query)
        cursor = (
            self._collection.find(query, projection=_EXCLUDE_ID)
            .skip(skip)
            .limit(limit)
            .sort("contacted_at", 1)
        )
        return total, list(cursor)