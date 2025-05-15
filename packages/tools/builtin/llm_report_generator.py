# packages/tools/builtin/llm_report_generator.py
"""
股票走势总结插件：调用语言模型（或内部算法）生成自然语言总结
"""

def summarize(df) -> str:
    first_price = df["收盘价"].iloc[0]
    last_price = df["收盘价"].iloc[-1]
    pct_change = ((last_price - first_price) / first_price) * 100

    trend = "上涨" if pct_change > 0 else "下跌"
    return f"在过去30天内，该股票整体呈现{trend}趋势，涨跌幅为 {pct_change:.2f}%。"

