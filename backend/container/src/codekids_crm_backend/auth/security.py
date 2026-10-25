from collections.abc import Callable, Mapping
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from google.auth.transport import requests as google_requests
from google.oauth2 import id_token as google_id_token

from codekids_crm_backend.auth.schemas import CurrentUser
from codekids_crm_backend.core.config import settings
from codekids_crm_backend.users.models import Role

JWT_ALGORITHM = "H256"

_google_request = google_requests.Request()
_bearer_scheme = HTTPBearer(auto_error=False)

class InvalidGoogleTokenError(Exception):
    pass

def _require_jwt_secret() -> str:
    if not settings.jwt_secret:
        raise RuntimeError(
            "JWT secret is not configured" # /secrets/jwt_secret.txt
        )
    return settings.jwt_secret

def verify_google_id_token(id_token: str) -> Mapping[str, Any]:
    # ตรวจสอบ Token กับ public key ของ Google
    try:
        payload = google_id_token.verify_oauth2_token(
            id_token, _google_request, settings.google_client_id
        )
    except ValueError as exc:
        raise InvalidGoogleTokenError(str(exc)) from exc

    if not payload.get("email_verified", False):
        raise InvalidGoogleTokenError("google account email is not verified")

    return payload

def create_access_token(*, user_id: str, email: str, role: Role) -> str:
    # ออก JWT ของระบบ CRM
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "email": email,
        "role": role,
        "iat": now,
        "exp": now + timedelta(minutes=settings.jwt_expire_minutes),
    }
    return jwt.encode(payload, _require_jwt_secret(), algorithm=JWT_ALGORITHM)

def decode_access_token(token: str) -> CurrentUser:
    try:
        payload = jwt.decode(token, _require_jwt_secret(), algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    return {
        "user_id": payload["sub"],
        "email": payload["email"],
        "role": Role(payload["role"]),
    }

def get_current_user(
    # deps สำหรับ route ที่ต้องการบังคับ login 
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer_scheme),
) -> CurrentUser:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return decode_access_token(credentials.credentials)

def require_role(*allowed_roles: Role) -> Callable[..., CurrentUser]:
    # deps สำหรับ route ที่ต้องการบังคับตรวจ role

    def _check_role(current_user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if current_user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="insufficient permission for this action",
            )
        return current_user

    return _check_role