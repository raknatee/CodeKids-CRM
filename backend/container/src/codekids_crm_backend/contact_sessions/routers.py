from fastapi import APIRouter, Depends, HTTPException, Query, status

from codekids_crm_backend.core.app_setting import BASE_PATH
from codekids_crm_backend.core.db import get_database
from codekids_crm_backend.contact_sessions.repository import (
    ContactSessionNotFoundError,
    ContactSessionRepository,
)
from codekids_crm_backend.contact_sessions.schemas import (
    ContactSessionCreate,
    ContactSessionListOut,
    ContactSessionOut,
    ContactSessionReplace,
)

contact_session_router = APIRouter()

contact_session_basepath = f"{BASE_PATH}/contact-session"


def get_repository() -> ContactSessionRepository:
    return ContactSessionRepository(get_database())


@contact_session_router.get(
    f"{contact_session_basepath}/list", response_model=ContactSessionListOut
)
def list_contact_session_endpoint(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    internal_id: str | None = Query(default=None),
    repo: ContactSessionRepository = Depends(get_repository),
) -> dict:
    total, items = repo.list(skip=skip, limit=limit, internal_id=internal_id)
    return {"total": total, "items": items}


@contact_session_router.get(contact_session_basepath, response_model=ContactSessionOut)
def get_contact_session_endpoint(
    session_id: str,
    repo: ContactSessionRepository = Depends(get_repository),
) -> ContactSessionOut:
    try:
        return repo.get_by_session_id(session_id)
    except ContactSessionNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@contact_session_router.post(
    contact_session_basepath,
    response_model=ContactSessionOut,
    status_code=status.HTTP_201_CREATED,
)
def add_contact_session_endpoint(
    new_session: ContactSessionCreate,
    repo: ContactSessionRepository = Depends(get_repository),
) -> ContactSessionOut:
    return repo.create(new_session)


@contact_session_router.put(contact_session_basepath, response_model=ContactSessionOut)
def edit_contact_session_endpoint(
    session_id: str,
    session: ContactSessionReplace,
    repo: ContactSessionRepository = Depends(get_repository),
) -> ContactSessionOut:
    try:
        return repo.replace(session_id, session)
    except ContactSessionNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc


@contact_session_router.delete(
    contact_session_basepath, status_code=status.HTTP_204_NO_CONTENT
)
def delete_contact_session_endpoint(
    session_id: str,
    repo: ContactSessionRepository = Depends(get_repository),
) -> None:
    try:
        repo.delete(session_id)
    except ContactSessionNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)
        ) from exc