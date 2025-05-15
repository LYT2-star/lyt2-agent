# packages/agents/resume_agent.py
"""
简历筛选智能体：负责解析简历内容、提取关键信息、生成评分
"""

from typing import Dict, Any
from packages.agents.base_agent import BaseAgent
from packages.tools.builtin import pdf_text_extractor, resume_parser, llm_scorer, excel_writer

class ResumeAgent(BaseAgent):
    def __init__(self):
        super().__init__(agent_id="resume_agent", name="简历智能体")

    def describe(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "description": "用于解析简历、提取字段并打分"
        }

    def run(self, task_input: Dict[str, Any]) -> Dict[str, Any]:
        file_bytes = task_input.get("file_bytes")
        job_type = task_input.get("job_type")
        username = task_input.get("username")

        # 1. 提取PDF文本
        raw_text = pdf_text_extractor.extract_text(file_bytes)

        # 2. 简历字段解析
        parsed_data = resume_parser.parse(raw_text)

        # 3. 调用大模型评分
        score_result = llm_scorer.score(parsed_data, job_type)

        # 4. 保存为CSV报告
        report_url = excel_writer.export_resume_report(username, parsed_data, score_result)

        return {
            "parsed": parsed_data,
            "score": score_result,
            "report_url": report_url
        }

