import streamlit as st
import pandas as pd
import json
import os

st.title("📄 今日推荐记录与命中回查")

def load_data():
    path = "logs/recommendations.jsonl"
    if not os.path.exists(path):
        st.warning("暂无推荐记录文件")
        return pd.DataFrame()
    with open(path, "r") as f:
        lines = f.readlines()
    data = [json.loads(l) for l in lines if l.strip()]
    return pd.DataFrame(data)

df = load_data()
if not df.empty:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp", ascending=False)
    st.dataframe(df, use_container_width=True)
else:
    st.info("暂无推荐记录")
