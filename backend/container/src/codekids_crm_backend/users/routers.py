from fastapi import APIRouter, Depends, HTTPException, Query, status

from codekids_crm_backend.auth.schemas import CurrentUser
from codekids_crm_backend.auth.security import require_role
from codekids_crm_backend.core.app_setting import BASE_PATH
from codekids_crm_backend.core.db import get_database
from codekids_crm_backend.users.models import Role
from codekids_crm_backend.users.repository import (
    UserAlreadyExistsError,
    UserNotFoundError,
    UserRepository,
)
from codekids_crm_backend.users.schemas import (
    UserCreate,
    UserListOut,
    UserOut,
    UserReplace,
)

user_router = APIRouter()

user_basepath = f"{BASE_PATH}/user"


def get_repository() -> UserRepository:
    return UserRepository(get_database())


@user_router.get(f"{user_basepath}/list", response_model=UserListOut)
def list_user_endpoint(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    repo: UserRepository = Depends(get_repository),
    _current: CurrentUser = Depends(require_role(Role.ADMIN)),
) -> dict:
    total, items = repo.list(skip=skip, limit=limit)
    return {"total": total, "items": items}


@user_router.get(user_basepath, response_model=UserOut)
def get_user_endpoint(
    user_id: str,
    repo: UserRepository = Depends(get_repository),
    _current: CurrentUser = Depends(require_role(Role.ADMIN)),
) -> UserOut:
    try:
        return repo.get_by_user_id(user_id)
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@user_router.post(
    user_basepath, response_model=UserOut, status_code=status.HTTP_201_CREATED
)
def add_user_endpoint(
    new_user: UserCreate,
    repo: UserRepository = Depends(get_repository),
    _current: CurrentUser = Depends(require_role(Role.ADMIN)),
) -> UserOut:
    try:
        return repo.create(new_user)
    except UserAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(exc)
        ) from exc


@user_router.put(user_basepath, response_model=UserOut)
def edit_user_endpoint(
    user_id: str,
    user: UserReplace,
    repo: UserRepository = Depends(get_repository),
    _current: CurrentUser = Depends(require_role(Role.ADMIN)),
) -> UserOut:
    try:
        return repo.replace(user_id, user)
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@user_router.delete(user_basepath, status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(
    user_id: str,
    repo: UserRepository = Depends(get_repository),
    _current: CurrentUser = Depends(require_role(Role.ADMIN)),
) -> None:
    try:
        repo.delete(user_id)
    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc