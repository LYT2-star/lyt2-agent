# packages/tools/builtin/excel_writer.py
"""
简历评分结果导出插件：将结果保存为 CSV 文件
"""

import csv
import os
import uuid

def export_resume_report(username: str, parsed: dict, score: dict) -> str:
    filename = f"{username}_resume_{uuid.uuid4().hex[:6]}.csv"
    save_path = os.path.join("static", "reports", filename)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["字段", "值"])
        for k, v in parsed.items():
            writer.writerow([k, v])
        writer.writerow(["评分", score["评分"]])
        writer.writerow(["评语", score["评语"]])

    return f"/static/reports/{filename}"

