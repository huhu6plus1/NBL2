import streamlit as st
import pandas as pd

st.title("📡 实时盘口抓取与推荐对比")

st.markdown("以下展示为模拟数据，后续可接TAB或365实时接口")

data = {
    "比赛": ["Jets vs Tuatara", "Waverley vs Diamond Valley"],
    "盘口": ["小182.5", "主队小92.5"],
    "赔率": [1.85, 1.90],
    "模型胜率": [0.58, 0.57],
    "EV估算": [6.3, 4.3],
    "是否推荐": ["✅", "✅"]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
