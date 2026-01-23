from fastapi import APIRouter, Depends, HTTPException, status, Header
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from typing import Annotated
import secrets

router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])

security = HTTPBasic()


@router.get("/basic-auth")
def demo_basic_auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
):
    return {
        "message": "Hi!",
        "username": credentials.username,
        "password": credentials.password,
    }


usernames_to_passwords = {
    "admin": "1",
    "rinat": "qwerty",
}


static_auth_token_to_username = {
    "95951270f8ad5d8fa9c0481ac4ea00b2": "admin",
    "017638e87b61148326040cc1804b77ba": "rinat",
}


def get_auth_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unvalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )

    correct_password = usernames_to_passwords.get(credentials.username, None)
    if correct_password is None:
        raise unauthed_exc

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        correct_password.encode("utf-8"),
    ):
        raise unauthed_exc

    return credentials.username


def get_username_by_static_auth_token(
    static_token: str = Header(alias="x-auth-token"),
) -> str:

    if username := static_auth_token_to_username.get(static_token):
        return username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="token invalid"
    )


@router.get("/basic-auth-username")
def demo_basic_auth_username(
    auth_username: str = Depends(get_auth_username),
):
    return {
        "message": f"Hi!, {auth_username}",
        "username": auth_username,
    }


@router.get("/some-http-header-auth")
def demo_auth_some_http_header(
    username: str = Depends(get_username_by_static_auth_token),
):
    return {
        "message": f"Hi!, {username}",
        "username": username,
    }
