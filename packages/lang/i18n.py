# packages/lang/i18n.py
"""
多语言国际化支持模块（初版）：
后续可扩展数据库或动态切换
"""

def get_text(key: str, lang: str = "zh") -> str:
    zh = {
        "login": "登录",
        "upload_resume": "上传简历",
        "submit": "提交任务",
        "logout": "退出登录",
    }

    en = {
        "login": "Login",
        "upload_resume": "Upload Resume",
        "submit": "Submit Task",
        "logout": "Logout",
    }

    lang_map = {"zh": zh, "en": en}
    return lang_map.get(lang, zh).get(key, key)

