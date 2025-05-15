# apps/api/services/task_service.py

from fastapi import UploadFile
from packages.core.executor import Executor
from packages.core.orchestrator import Orchestrator
from packages.agents.resume_agent import ResumeAgent
from packages.agents.stock_agent import StockAgent

# 初始化调度器与 Agent 注册
orchestrator = Orchestrator()
orchestrator.register_agent(ResumeAgent())
orchestrator.register_agent(StockAgent())
executor = Executor(orchestrator)

async def handle_resume_task(file: UploadFile, job_type: str, username: str):
    file_bytes = await file.read()
    return executor.execute_resume_task(file_bytes, job_type, username)

async def handle_stock_task(symbol: str, username: str):
    return executor.execute_stock_task(symbol, username)

