from datetime import datetime

from pydantic import BaseModel, ConfigDict

from codekids_crm_backend.customers.models import Experience, LeadStatus


class CustomerCreate(BaseModel):
    """Payload ตอนสร้างลูกค้าใหม่ (POST) — client ไม่ส่ง uid/updated_at เอง"""

    codekids_id: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    nickname: str | None = None
    dob: datetime | None = None
    email: str | None = None
    phone: str | None = None
    district: str | None = None
    city: str | None = None
    education: str | None = None
    workplace: str | None = None
    lead_status: LeadStatus = LeadStatus.NEW_LEAD
    experience: Experience | None = None
    notes: str | None = None
    why_codekids: str | None = None


class CustomerReplace(CustomerCreate):
    """ใช้กับ PUT (แทนที่ข้อมูลทั้งก้อน) โครงสร้างเหมือน Create ทุกประการ — ไม่ต้องเขียน field ซ้ำ"""


class CustomerOut(CustomerCreate):
    """Response ที่ส่งกลับ client และเป็นรูปแบบที่เก็บลง Mongo — เหมือน Create ทุกอย่าง บวก uid/updated_at ที่ server generate เอง"""

    model_config = ConfigDict(from_attributes=True)

    uid: str
    updated_at: datetime


class CustomerListOut(BaseModel):
    """Response แบบมี pagination สำหรับ endpoint list"""

    total: int
    items: list[CustomerOut]