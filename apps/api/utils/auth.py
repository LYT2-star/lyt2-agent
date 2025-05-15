# apps/api/utils/auth.py

from fastapi import Header, HTTPException

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token格式错误")
    token = authorization.split(" ")[1]
    # 可替换为 Token 解密逻辑
    return "mock_user"

def get_current_admin_user(authorization: str = Header(...)):
    user = get_current_user(authorization)
    # 可校验权限角色
    if user != "admin":
        raise HTTPException(status_code=403, detail="权限不足")
    return user

