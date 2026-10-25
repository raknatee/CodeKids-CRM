from datetime import datetime
from typing import NotRequired, TypedDict

from codekids_crm_backend.users.models import Role


class UserCreate(TypedDict):
    """Payload ตอน admin ลงทะเบียน user ใหม่ไว้ล่วงหน้าก่อนเจ้าตัวจะ Google login ครั้งแรก"""
    email: str
    role: Role
    name: NotRequired[str | None]
    is_active: NotRequired[bool]

class UserReplace(UserCreate):
    """ใช้กับ PUT ไม่รวม google_sub/last_login_at"""

class UserOut(UserCreate):
    """รูปแบบที่ตอบกลับ client และเก็บลง Mongo"""
    user_id: str
    google_sub: NotRequired[str | None]
    created_at: datetime
    updated_at: datetime
    last_login_at: NotRequired[datetime | None]

class UserListOut(TypedDict):
    total: int
    items: list[UserOut]