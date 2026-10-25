from fastapi import APIRouter, Depends, HTTPException, status

from codekids_crm_backend.auth.schemas import CurrentUser, GoogleLoginRequest, TokenResponse
from codekids_crm_backend.auth.security import (
    InvalidGoogleTokenError,
    create_access_token,
    get_current_user,
    verify_google_id_token,
)
from codekids_crm_backend.core.app_setting import BASE_PATH
from codekids_crm_backend.core.db import get_database
from codekids_crm_backend.users.repository import UserRepository

auth_router = APIRouter()

auth_basepath = f"{BASE_PATH}/auth"


def get_repository() -> UserRepository:
    return UserRepository(get_database())


@auth_router.post(f"{auth_basepath}/google/login", response_model=TokenResponse)
def google_login_endpoint(
    body: GoogleLoginRequest,
    repo: UserRepository = Depends(get_repository),
) -> TokenResponse:
    try:
        google_payload = verify_google_id_token(body["id_token"])
    except InvalidGoogleTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid google token"
        ) from exc

    email = google_payload["email"]
    user = repo.get_by_email(email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="this email has not been registered by an admin",
        )
    if not user.get("is_active", True):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="this account has been deactivated",
        )

    user = repo.record_google_login(email=email, google_sub=google_payload["sub"])

    access_token = create_access_token(
        user_id=user["user_id"], email=user["email"], role=user["role"]
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user["role"],
        "email": user["email"],
    }


@auth_router.get(f"{auth_basepath}/me", response_model=CurrentUser)
def get_me_endpoint(current_user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
    return current_user