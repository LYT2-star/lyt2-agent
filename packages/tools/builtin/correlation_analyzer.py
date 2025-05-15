# packages/tools/builtin/correlation_analyzer.py
"""
相关性分析插件：对股票收盘数据进行简单分析
"""

def analyze(df):
    if "收盘价" not in df.columns:
        return {"error": "数据中不包含收盘价字段"}
    
    max_price = df["收盘价"].max()
    min_price = df["收盘价"].min()
    pct_change = ((df["收盘价"].iloc[-1] - df["收盘价"].iloc[0]) / df["收盘价"].iloc[0]) * 100

    return {
        "最高价": round(max_price, 2),
        "最低价": round(min_price, 2),
        "近30日涨跌幅": f"{pct_change:.2f}%"
    }

