# packages/tools/builtin/html_report_builder.py
"""
股票分析报告构建插件：将图表和总结生成HTML报告页面
"""

import os
import uuid

def build(symbol, chart_paths, summary):
    html_dir = "static/reports"
    os.makedirs(html_dir, exist_ok=True)

    filename = f"{symbol}_report_{uuid.uuid4().hex[:6]}.html"
    full_path = os.path.join(html_dir, filename)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(f"<html><head><title>{symbol} 股票分析报告</title></head><body>")
        f.write(f"<h1>{symbol} 股票分析报告</h1>")
        f.write(f"<p>{summary}</p>")
        for chart in chart_paths:
            f.write(f'<img src="{chart}" width="600"><br>')
        f.write("</body></html>")

    return f"/static/reports/{filename}"

