# apps/api/schemas/user_schema.py

from pydantic import BaseModel

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

