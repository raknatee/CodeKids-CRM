from datetime import datetime
from typing import NotRequired, TypedDict

from .model import ContactType, Requirement


class ContactSessionCreate(TypedDict):
    """Payload POST contact session
    internal_id และ contacted_at บังคับส่งมาเสมอ"""

    internal_id: str
    contacted_at: datetime
    platform_id: NotRequired[str | None]
    admin_responded_at: NotRequired[datetime | None]
    followup_tag: NotRequired[str | None]
    requirement: NotRequired[Requirement | None]
    contact_type: NotRequired[ContactType | None]
    insight: NotRequired[str | None]
    session_notes: NotRequired[str | None]

class ContactSessionReplace(ContactSessionCreate):
    """ใช้กับ PUT (แทนที่ข้อมูลทั้งก้อน)"""

class ContactSessionOut(ContactSessionCreate):
    """รูปแบบที่ตอบกลับ client และเก็บลง Mongo"""

    session_id: str
    updated_at: datetime

class ContactSessionListOut(TypedDict):
    """Pagination response สำหรับ endpoint list"""

    total: int
    items: list[ContactSessionOut]