# packages/tools/builtin/chart_generator.py
"""
图表生成插件：将股票收盘数据生成趋势图表（matplotlib）
"""

import os
import uuid
import matplotlib.pyplot as plt

def generate_charts(df, symbol):
    chart_dir = "static/charts"
    os.makedirs(chart_dir, exist_ok=True)
    
    filename = f"{symbol}_{uuid.uuid4().hex[:6]}.png"
    path = os.path.join(chart_dir, filename)

    plt.figure(figsize=(10, 4))
    plt.plot(df["日期"], df["收盘价"], marker="o")
    plt.title(f"{symbol} 股票走势")
    plt.xlabel("日期")
    plt.ylabel("收盘价")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

    return [f"/static/charts/{filename}"]

