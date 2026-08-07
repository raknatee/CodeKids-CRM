import os

class Settings:
    mongo_uri: str = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
    mongo_db_name: str = os.environ.get("MONGO_DB_NAME", "codekids_crm")

settings = Settings()