# packages/core/executor.py
"""
任务执行器：根据任务规划结果，调用调度器执行Agent任务
"""

from typing import Dict
from packages.core.orchestrator import Orchestrator
from packages.core.planner import Planner

class Executor:
    def __init__(self, orchestrator: Orchestrator):
        self.planner = Planner()
        self.orchestrator = orchestrator

    def execute_resume_task(self, file_bytes: bytes, job_type: str, username: str) -> Dict:
        task_plan = self.planner.plan_resume_task(job_type)
        agent_id = task_plan["agent_id"]
        task_input = {
            "file_bytes": file_bytes,
            "job_type": job_type,
            "username": username
        }
        return self.orchestrator.run_agent(agent_id, task_input)

    def execute_stock_task(self, symbol: str, username: str) -> Dict:
        task_plan = self.planner.plan_stock_task(symbol)
        agent_id = task_plan["agent_id"]
        task_input = {
            "symbol": symbol,
            "username": username
        }
        return self.orchestrator.run_agent(agent_id, task_input)

