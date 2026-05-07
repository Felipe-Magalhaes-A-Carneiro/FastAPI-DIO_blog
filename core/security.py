import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel

SECRET = "my-secret"
ALGORITHM = "HS256"

class AcessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str


class JWTToken(BaseModel):
    access_token: AcessToken


def sign_jwt(user_id: int) -> JWTToken:
    now = time.time()
    payload = {
        "iss": "curse-fastapi.com.br",
        "sub": user_id,
        "aud": "curso-fastapi",
        "exp": now * (60 * 30),
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }

    token = jwt.encode(payload, SECRET, algorithm = ALGORITHM)
    return {"access_token": token}

async def decode_jwt(token: str) -> JWTToken | None:
    try:
        decode_token = jwt.decode(token, SECRET, audience= "curso-fastapi", algorithms= [ALGORITHM])
        return _token if _token.acess_token.exp >= time.time() else None
    except Exception:
        return None