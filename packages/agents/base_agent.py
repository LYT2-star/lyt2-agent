# packages/agents/base_agent.py
"""
Agent 抽象基类：所有 Agent 都应继承此类并实现 run() 方法
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    def __init__(self, agent_id: str, name: str = "UnnamedAgent"):
        self.agent_id = agent_id
        self.name = name

    @abstractmethod
    def describe(self) -> Dict[str, Any]:
        """
        返回 Agent 的功能描述
        """
        pass

    @abstractmethod
    def run(self, task_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行任务，返回结果
        """
        pass

    def __str__(self):
        return f"<Agent {self.name} ({self.agent_id})>"

