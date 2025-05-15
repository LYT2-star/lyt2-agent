# packages/core/orchestrator.py
"""
调度器：用于调度多个 Agent，并分配任务执行顺序
"""

from typing import List, Dict
from packages.agents.base_agent import BaseAgent

class Orchestrator:
    def __init__(self):
        self.registered_agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        self.registered_agents[agent.agent_id] = agent

    def get_agent(self, agent_id: str) -> BaseAgent:
        return self.registered_agents.get(agent_id)

    def run_agent(self, agent_id: str, task_input: Dict) -> Dict:
        agent = self.get_agent(agent_id)
        if not agent:
            return {"error": f"Agent {agent_id} not found."}
        return agent.run(task_input)

    def list_agents(self) -> List[str]:
        return list(self.registered_agents.keys())

