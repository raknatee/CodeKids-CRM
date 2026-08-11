from typing import TypedDict

from fastapi import APIRouter, Depends, HTTPException, Query, status

from codekids_crm_backend.core.app_setting import BASE_PATH
from codekids_crm_backend.core.db import get_database
from codekids_crm_backend.customers.repository import (
    CustomerNotFoundError,
    CustomerRepository,
)
from codekids_crm_backend.customers.schemas import (
    CustomerCreate,
    CustomerListOut,
    CustomerOut,
    CustomerReplace,
)

customer_router = APIRouter()

customer_basepath = f"{BASE_PATH}/customer"


class WhyCodeKidsResponse(TypedDict):
    options: list[str]

def get_repository() -> CustomerRepository:
    return CustomerRepository(get_database())

@customer_router.get(f"{customer_basepath}/whycodekids")
def get_why_codekids_options_endpoint() -> WhyCodeKidsResponse:
    return {
        "options": [
            "ADS", "TIKTOK", "COMMENT_RESPONSE", "WORD_OF_MOUTH"
            ]
    }

@customer_router.get(customer_basepath, response_model=CustomerOut)
def get_customer_endpoint(
    uid: str,
    repo: CustomerRepository = Depends(get_repository), ) -> CustomerOut:
    try:
        return repo.get_by_uid(uid)
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc

@customer_router.post(customer_basepath, response_model=CustomerOut, status_code=status.HTTP_201_CREATED)
def add_costomer_endpoint(
    new_customer: CustomerCreate,
    repo: CustomerRepository = Depends(get_repository), ) -> CustomerOut:
        return repo.create(new_customer)

@customer_router.put(customer_basepath, response_model=CustomerOut)
def edit_customer_endpoint(
     uid: str,
     customer: CustomerReplace,
     repo: CustomerRepository = Depends(get_repository), ) -> CustomerOut:
     try:
          return repo.replace(uid, customer)
     except CustomerNotFoundError as exc:
          raise HTTPException(
               status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
          ) from exc

@customer_router.delete(customer_basepath, status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_endpoint(
    uid: str,
    repo: CustomerRepository = Depends(get_repository), ) -> None:
    try:
        repo.delete(uid)
    except CustomerNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc