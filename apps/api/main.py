# apps/api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.api.routers import task_router, plugin_router, user_router

app = FastAPI(
    title="羚羊T2 AI Agent 后端接口",
    version="1.0.0",
    description="提供任务管理、插件管理、用户认证等接口"
)

# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(user_router.router, prefix="/api/user", tags=["用户管理"])
app.include_router(task_router.router, prefix="/api/task", tags=["任务管理"])
app.include_router(plugin_router.router, prefix="/api/plugin", tags=["插件管理"])

@app.get("/api/healthcheck")
async def healthcheck():
    return {"status": "ok"}

