import streamlit as st
from PIL import Image
import random

st.title("📤 上传盘口截图并自动识别分析")

uploaded = st.file_uploader("上传TAB或Bet365盘口截图", type=["png", "jpg", "jpeg"])
if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="上传的盘口截图", use_column_width=True)

    st.subheader("识别结果（模拟OCR）")
    # 模拟识别结果
    line = random.choice([182.5, 183.5, 181.5])
    odds = random.choice([1.85, 1.90, 1.88])
    ev = round((odds * 0.55 - 0.45) * 100, 2)
    st.write(f"识别盘口：小{line} @ {odds}")
    st.write(f"预估胜率：55%")
    st.success(f"预估EV值：{ev}%")
    if ev > 3:
        st.markdown("✅ **推荐下注：小分方向具备正EV价值**")
    else:
        st.markdown("⚠️ **EV偏低，建议观望**")
