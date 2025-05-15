# packages/tools/builtin/llm_scorer.py
"""
简历评分插件：将简历结构化内容发送给大模型，生成匹配得分
"""

def score(parsed_resume: dict, job_type: str = "运营") -> dict:
    # 模拟评分逻辑，可对接大模型API
    base_score = 60
    skill_bonus = len(parsed_resume.get("技能", [])) * 5
    score = base_score + skill_bonus
    return {
        "岗位": job_type,
        "评分": min(score, 100),
        "评语": "技能匹配良好，建议进入面试流程。" if score > 75 else "技能匹配一般，可考虑培养。"
    }

