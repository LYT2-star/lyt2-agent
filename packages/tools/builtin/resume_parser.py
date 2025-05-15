# packages/tools/builtin/resume_parser.py
"""
简历解析插件：从原始文本中提取结构化信息
"""

import re

def parse(text: str) -> dict:
    result = {
        "姓名": "",
        "电话": "",
        "邮箱": "",
        "学历": "",
        "技能": []
    }
    # 示例逻辑（可根据简历模板优化）
    name_match = re.search(r"姓名[:：]?\s*(\S+)", text)
    phone_match = re.search(r"1[3-9]\d{9}", text)
    email_match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

    if name_match:
        result["姓名"] = name_match.group(1)
    if phone_match:
        result["电话"] = phone_match.group()
    if email_match:
        result["邮箱"] = email_match.group()

    if "研究生" in text:
        result["学历"] = "研究生"
    elif "本科" in text:
        result["学历"] = "本科"
    else:
        result["学历"] = "未知"

    skills = []
    for keyword in ["Python", "数据分析", "SQL", "机器学习", "PPT"]:
        if keyword in text:
            skills.append(keyword)
    result["技能"] = skills

    return result

