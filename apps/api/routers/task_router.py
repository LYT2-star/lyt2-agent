# apps/api/routers/task_router.py
from fastapi import APIRouter, UploadFile, File, Form, Depends
from apps.api.schemas.task_schema import TaskSubmitResponse
from apps.api.services.task_service import handle_resume_task, handle_stock_task
from apps.api.utils.auth import get_current_user

router = APIRouter()

@router.post("/resume", response_model=TaskSubmitResponse)
async def submit_resume_task(file: UploadFile = File(...), job_type: str = Form("运营"), username: str = Depends(get_current_user)):
    task_result = await handle_resume_task(file, job_type, username)
    return task_result

@router.post("/stock", response_model=TaskSubmitResponse)
async def submit_stock_task(symbol: str = Form(...), username: str = Depends(get_current_user)):
    task_result = await handle_stock_task(symbol, username)
    return task_result

