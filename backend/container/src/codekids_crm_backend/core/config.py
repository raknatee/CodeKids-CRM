import os
from pathlib import Path

def _read_secret_file(path: str) -> str | None:

    """
    อ่านค่าจาก docker secret file (ตอน deploy จริง)
    path ของไฟล์มาจาก env var
    """

    if path and Path(path).is_file():
        return Path(path).read_text().strip()
    return None

class Settings:
    # อ่านค่า config จาก environment variable / docker secrets
    
    mongo_host: str = os.environ.get("MONGO_HOST", "coredb")
    mongo_port: str = os.environ.get("MONGO_PORT", "27017")
    mongo_db_name: str = os.environ.get("MONGO_DB_NAME", "codekids_crm")
    mongo_auth_source: str = os.environ.get("MONGO_AUTH_SOURCE", "admin")

    mongo_user: str | None = _read_secret_file("/run/secrets/mongo_db_user.txt")
    mongo_password: str | None = _read_secret_file("/run/secrets/mongo_db_password.txt")

    @property
    def mongo_uri(self) -> str:
        if self.mongo_user and self.mongo_password:
            return (
                f"mongodb://{self.mongo_user}:{self.mongo_password}"
                f"@{self.mongo_host}:{self.mongo_port}"
                # f"@{self.mongo_host}:{self.mongo_port}/?authSource{self.mongo_auth_source}"
            )
        # Fallback Run Local ตรงๆ ไม่มี Auth
        return f"mongodb://{self.mongo_host}:{self.mongo_port}"

settings = Settings()