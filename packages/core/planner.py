# packages/core/planner.py
"""
任务规划器：用于解析用户自然语言任务指令，并转换为结构化任务请求
"""

from typing import Dict

class Planner:
    def __init__(self):
        pass

    def plan_resume_task(self, job_type: str) -> Dict:
        return {
            "agent_id": "resume_agent",
            "task_type": "resume",
            "job_type": job_type
        }

    def plan_stock_task(self, symbol: str) -> Dict:
        return {
            "agent_id": "stock_agent",
            "task_type": "stock",
            "symbol": symbol
        }

