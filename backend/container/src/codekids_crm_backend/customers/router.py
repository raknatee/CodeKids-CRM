from typing import TypedDict

from fastapi import APIRouter

from codekids_crm_backend.core.app_setting import BASE_PATH
from codekids_crm_backend.customers.models import CustomerModel

customer_router = APIRouter()

customer_basepath = f"{BASE_PATH}/customer"


class WhyCodeKidsResponse(TypedDict):
    options: list[str]

@customer_router.get(f"{customer_basepath}/whycodekids")
def get_why_codekids_options_endpoint()->WhyCodeKidsResponse:
    return {
        "options": [
            "abs", "tiktok", "comment_response", "word_of_mouth"
        ]
    }
    
    
@customer_router.get(f"{customer_basepath}")
def get_customer_endpoint(uid: str)->CustomerModel:
    pass

@customer_router.post(f"{customer_basepath}")
def add_customer_endpoint(new_customer: CustomerModel):
    pass

@customer_router.put(f"{customer_basepath}")
def edit_customer_endpoint(uid: str, customer: CustomerModel):
    pass