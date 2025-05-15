# packages/tools/tool_base.py
"""
插件基类定义：所有插件必须继承该类并实现 run() 方法
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

class ToolBase(ABC):
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, inputs: Dict[str, Any]) -> Any:
        """
        执行插件主逻辑
        参数:
            inputs: 插件执行输入参数字典
        返回:
            任意执行结果
        """
        pass

