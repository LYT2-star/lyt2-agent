插件结构要求

上传插件必须是 .zip 压缩包，包含以下结构：

plugin_name.zip
├── tool.py             # 插件主逻辑
└── metadata.json       # 插件元信息（名称、描述、作者等）

tool.py 必须包含：
from packages.tools.tool_base import ToolBase

class YourPlugin(ToolBase):
    def run(self, inputs):
        # 插件逻辑处理
        return result

metadata.json 示例：
{
  "name": "resume_highlighter",
  "description": "从简历中提取亮点关键词",
  "author": "马天亮"
}

上传方式

前端插件管理页 → 选择 .zip 文件 → 上传
或使用接口 POST /plugin/upload，需携带 Token

上传成功后可启用/禁用插件，并由 Agent 自动识别调用
