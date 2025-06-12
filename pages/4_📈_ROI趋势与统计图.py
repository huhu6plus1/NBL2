import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import os

st.title("📈 ROI 趋势图表分析")

def load_data():
    path = "logs/recommendations.jsonl"
    if not os.path.exists(path):
        return pd.DataFrame()
    with open(path, "r") as f:
        lines = f.readlines()
    data = [json.loads(l) for l in lines if l.strip()]
    return pd.DataFrame(data)

df = load_data()
if df.empty or "ev" not in df.columns:
    st.warning("暂无足够数据绘图")
else:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    roi = (df["ev"].cumsum()) / (df.index + 1)
    fig, ax = plt.subplots()
    ax.plot(df["timestamp"], roi, marker='o')
    ax.set_title("ROI累计趋势")
    ax.set_ylabel("累计ROI (%)")
    ax.set_xlabel("时间")
    st.pyplot(fig)
