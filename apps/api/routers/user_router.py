# apps/api/routers/user_router.py
from fastapi import APIRouter, Depends, HTTPException
from apps.api.schemas.user_schema import UserLoginRequest, UserLoginResponse
from apps.api.services.user_service import authenticate_user, create_access_token

router = APIRouter()

@router.post("/login", response_model=UserLoginResponse)
async def login(user: UserLoginRequest):
    user_obj = authenticate_user(user.username, user.password)
    if not user_obj:
        raise HTTPException(status_code=400, detail="用户名或密码错误")
    token = create_access_token(data={"sub": user.username})
    return UserLoginResponse(access_token=token, token_type="bearer")

