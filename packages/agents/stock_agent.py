# packages/agents/stock_agent.py
"""
股票分析智能体：负责获取行情数据、分析走势、生成图表与解读
"""

from typing import Dict, Any
from packages.agents.base_agent import BaseAgent
from packages.tools.builtin import stock_data_fetcher, correlation_analyzer, chart_generator, llm_report_generator, html_report_builder

class StockAgent(BaseAgent):
    def __init__(self):
        super().__init__(agent_id="stock_agent", name="股票智能体")

    def describe(self) -> Dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "description": "用于获取股票数据、分析相关性并生成图文报告"
        }

    def run(self, task_input: Dict[str, Any]) -> Dict[str, Any]:
        symbol = task_input.get("symbol")
        username = task_input.get("username")

        # 1. 获取股票行情
        stock_df = stock_data_fetcher.fetch(symbol)

        # 2. 分析数据相关性
        analysis_result = correlation_analyzer.analyze(stock_df)

        # 3. 生成图表
        chart_paths = chart_generator.generate_charts(stock_df, symbol)

        # 4. 调用大模型生成解读文本
        summary = llm_report_generator.summarize(stock_df)

        # 5. 输出成HTML报告
        report_url = html_report_builder.build(symbol, chart_paths, summary)

        return {
            "symbol": symbol,
            "charts": chart_paths,
            "summary": summary,
            "report_url": report_url
        }

