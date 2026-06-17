import hashlib
import hmac
import secrets
import time

from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel

router = APIRouter()

_tokens: dict[str, dict] = {}

SECRET = "change-me-in-production"
TOKEN_TTL = 72 * 3600


class LoginRequest(BaseModel):
      username: str
      api_key: str


@router.post("/token")
async def create_token(data: LoginRequest):
      expected = hashlib.sha256(f"{data.username}:{SECRET}".encode()).hexdigest()
      if not hmac.compare_digest(da
