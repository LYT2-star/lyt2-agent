# packages/tools/builtin/stock_data_fetcher.py
"""
股票数据获取插件：获取某个股票的历史行情数据
支持模拟数据（可扩展接入新浪、Yahoo等API）
"""

import pandas as pd
from datetime import datetime, timedelta

def fetch(symbol: str) -> pd.DataFrame:
    # 生成模拟数据：过去30天的价格数据
    dates = pd.date_range(end=datetime.today(), periods=30)
    prices = [100 + i * 0.5 + (i % 5) * 2 for i in range(30)]  # 模拟价格波动

    df = pd.DataFrame({
        "日期": dates,
        "收盘价": prices
    })
    df["股票代码"] = symbol.upper()
    return df

