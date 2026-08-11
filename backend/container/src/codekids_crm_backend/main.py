from fastapi import FastAPI

from codekids_crm_backend.customers.routers import customer_router

app = FastAPI()

app.include_router(customer_router)


@app.get("/api/backend")
def read_root():
    return {"Hello": "World"}