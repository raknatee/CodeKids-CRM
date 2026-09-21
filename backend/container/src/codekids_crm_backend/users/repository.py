import uuid

from pymongo.database import Database
from pymongo.collection import Collection

from codekids_crm_backend.users.schemas import UserCreate, UserOut, UserReplace

from datetime import datetime, timezone

COLLECTION_NAME = "users"
_EXCLUDE_ID = {"_id": 0}


class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserRepository:
    def __init__(self, db: Database) -> None:
        self._db = db
        self._collection: Collection = db[COLLECTION_NAME]

    def create(self, payload: UserCreate) -> UserOut:
        if self._collection.find_one({"email": payload["email"]}, projectiion=_EXCLUDE_ID):
            raise UserAlreadyExistsError(f"user email={payload['email']} already exists")

        now = datetime.now(timezone.utc)
        doc: UserOut = {
            "is_active": True,
            **payload,
            "user_id": str(uuid.uuid4()),
            "created_at": now,
            "updated_at": now,
        }
        self._collection.insert_one(dict(doc))
        return doc

    def get_by_user_id(self, user_id: str) -> UserOut:
        doc = self._collection.find_one({"user_id": user_id}, projection=_EXCLUDE_ID)
        if doc is None:
            raise UserNotFoundError(f"user user_id={user_id} not found")
        return doc

    

    def get_by_email(self, email: str) -> UserOut | None:
        return self._collection.find_one({"email": email}, projection=_EXCLUDE_ID)

    def replace(self, user_id: str, payload: UserReplace) -> UserOut:
        update_fields: dict = {**payload, "update_at": datetime.now(timezone.utc)}

        doc = self._collection.find_one_and_update(
            {"user_id": user_id},
            {"$set": update_fields},
            projection=_EXCLUDE_ID,
            return_document=True
        )
        if doc is None:
            raise UserNotFoundError(f"user user_id={user_id} not found")
        return doc
        

    def delete(self, user_id: str) -> None:
        result = self._collection.delete_one({"user_id": user_id})
        if result.deleted_count == 0:
            raise UserNotFoundError(f"user user_id={user_id} not found")

    def record_google_login(self, email: str, google_sub: str) -> UserOut:
        now = datetime.now(timezone.utc)
        doc = self._collection.find_one_and_update(
            {"email": email},
            {"$set": {"google_sub": google_sub, "last_login_at": now, "update_at": now}},
            projection=_EXCLUDE_ID,
            return_document=True,
        )

        if doc is None:
            raise UserNotFoundError(f"user email={email} not found")
        return doc





    