from fastapi import FastAPI

from codekids_crm_backend.core.app_setting import BASE_PATH
from codekids_crm_backend.customers.routers import customer_router

app = FastAPI(docs_url=BASE_PATH+'/docs',
              openapi_url=BASE_PATH+"openapi.json"
              )

app.include_router(customer_router)

