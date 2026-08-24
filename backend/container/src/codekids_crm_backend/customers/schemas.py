from datetime import datetime
from typing import NotRequired, TypedDict

from codekids_crm_backend.customers.models import Experience, LeadStatus


class CustomerCreate(TypedDict):
    """Payload ตอนสร้างลูกค้าใหม่ (POST) — client ไม่ส่ง uid/updated_at เอง
    """
    # NotRequired เผื่อ Client ส่ง Key มาไม่ครบ

    codekids_id: NotRequired[str | None]
    first_name: NotRequired[str | None]
    last_name: NotRequired[str | None]
    nickname: NotRequired[str | None]
    dob: NotRequired[datetime | None]
    email: NotRequired[str | None]
    phone: NotRequired[str | None]
    district: NotRequired[str | None]
    city: NotRequired[str | None]
    education: NotRequired[str | None]
    workplace: NotRequired[str | None]
    lead_status: NotRequired[LeadStatus]
    experience: NotRequired[Experience | None]
    notes: NotRequired[str | None]
    why_codekids: NotRequired[str | None]


class CustomerReplace(CustomerCreate):
    """ใช้กับ PUT (แทนที่ข้อมูลทั้งก้อน) โครงสร้างเหมือน Create ทุกประการ — ไม่ต้องเขียน field ซ้ำ"""


class CustomerOut(CustomerCreate):
    """Response ที่ส่งกลับ client และเป็นรูปแบบที่เก็บลง Mongo — เหมือน Create ทุกอย่าง บวก uid/updated_at ที่ server generate เอง"""

    uid: str
    updated_at: datetime


class CustomerListOut(TypedDict):
    """Response แบบมี pagination สำหรับ endpoint list"""

    total: int
    items: list[CustomerOut]