import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="NBL EV 推荐系统", layout="wide")
st.title("🏀 NBL1 + NZ NBL 自动推荐系统 v2.2")

st.markdown("🟢 自动推荐 + EV计算 + 推送 + 写入记录")

LOG_FILE = "logs/recommendations.jsonl"

def load_data():
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    data = [json.loads(line) for line in lines if line.strip()]
    return pd.DataFrame(data)

df = load_data()

if df.empty:
    st.warning("暂无推荐记录")
else:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp", ascending=False)

    def highlight_ev(val):
        try:
            return 'background-color: #ffe599' if float(val) >= 5 else ''
        except:
            return ''

    st.subheader("📄 最近推荐记录")
    styled_df = df.style.applymap(highlight_ev, subset=["ev"])
    st.dataframe(styled_df, use_container_width=True)
