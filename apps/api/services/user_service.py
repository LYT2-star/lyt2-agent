# ✅ apps/api/services/user_service.py
from apps.api.schemas.user_schema import UserLoginRequest
from apps.api.utils.security import hash_password

def authenticate_user(username: str, password: str):
    # ⚠️ 这里是模拟用户验证，可替换数据库查询逻辑
    if username == "admin" and password == "123456":
        return {"username": username}
    return None

def create_access_token(data: dict):
    # ⚠️ 示例用静态Token，生产环境建议用JWT
    return "mocked.jwt.token"
