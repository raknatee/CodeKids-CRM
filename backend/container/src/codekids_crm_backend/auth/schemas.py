from typing import TypedDict

from codekids_crm_backend.users.models import Role

class GoogleLoginRequest(TypedDict):
    id_token: str

class TokenResponse(TypedDict):
    access_token: str
    token_type: str
    role: Role
    email: str

class  CurrentUser(TypedDict):
    user_id: str
    email: str
    role: Role

