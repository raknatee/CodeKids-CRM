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