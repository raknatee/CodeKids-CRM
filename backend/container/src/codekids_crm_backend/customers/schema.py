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
    """ใช้กับ PUT (แทนที่ข้อมูลทั้งก้อน) โครงสร้างเหมือน Create ทุกประการ"""


class CustomerOut(BaseModel):
    """Response ที่ส่งกลับให้ client"""

    model_config = ConfigDict(from_attributes=True)

    uid: str
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


class CustomerListOut(BaseModel):
    """Response แบบมี pagination สำหรับ endpoint list"""

    total: int
    items: list[CustomerOut]