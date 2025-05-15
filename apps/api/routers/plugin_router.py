# apps/api/routers/plugin_router.py
from fastapi import APIRouter, UploadFile, File, Depends
from apps.api.services.plugin_service import upload_plugin, list_plugins, enable_plugin, disable_plugin
from apps.api.utils.auth import get_current_admin_user

router = APIRouter()

@router.post("/upload")
async def upload_plugin_file(file: UploadFile = File(...), admin_user: str = Depends(get_current_admin_user)):
    return await upload_plugin(file)

@router.get("/list")
async def get_plugin_list():
    return list_plugins()

@router.post("/enable/{plugin_name}")
async def enable_plugin_api(plugin_name: str, admin_user: str = Depends(get_current_admin_user)):
    return enable_plugin(plugin_name)

@router.post("/disable/{plugin_name}")
async def disable_plugin_api(plugin_name: str, admin_user: str = Depends(get_current_admin_user)):
    return disable_plugin(plugin_name)

