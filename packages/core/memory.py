# packages/core/memory.py
"""
上下文记忆模块（可扩展）：目前记录用户历史任务，未来可接入数据库
"""

from typing import List, Dict

class Memory:
    def __init__(self):
        self.user_task_history: Dict[str, List[Dict]] = {}

    def save_task(self, username: str, task_info: Dict):
        if username not in self.user_task_history:
            self.user_task_history[username] = []
        self.user_task_history[username].append(task_info)

    def get_history(self, username: str) -> List[Dict]:
        return self.user_task_history.get(username, [])

