from datetime import datetime
from enum import StrEnum
from typing import TypedDict


class LeadStatus(StrEnum):
    NEW_LEAD = "NEW_LEAD"
    OLD_LEAD = "OLD_LEAD"
    OLD_CUSTOMER = "OLD_CUSTOMER"


class Experience(StrEnum):
    EVER = "EVER"
    LITTLE = "LITTLE"
    NEVER = "NEVER"


class CustomerModel(TypedDict):
    """
    - `_id`: ObjectId ที่ Mongo gen ให้อัตโนมัติ (primary key จริงของ document)
    - `uid`: int อ้างอิงภายใน gen เองแบบ auto-increment (ผ่าน counters collection)
      ใช้เป็นรหัสที่ entity อื่น (SocialAccount, ContactSession ฯลฯ) จะมาอ้างอิงในอนาคต
    """

    uid: int
    codekids_id: str | None
    first_name: str | None
    last_name: str | None
    nickname: str | None
    dob: datetime | None
    email: str | None
    phone: str | None
    district: str | None
    city: str | None
    education: str | None
    workplace: str | None
    lead_status: LeadStatus
    experience: Experience | None
    notes: str | None
    why_codekids: str | None
    updated_at: datetime