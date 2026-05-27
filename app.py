import streamlit as st

st.set_page_config(page_title="Opti-Meal", layout="wide")

# -------- MAIN UI --------
st.markdown("""
<h1 style='text-align:center;'>🍏 Opti-Meal</h1>
<h3 style='text-align:center;'>AI Food Intelligence System</h3>
<p style='text-align:center; color:gray;'>Use the sidebar to navigate through the app</p>
""", unsafe_allow_html=True)

st.markdown("---")

# -------- FEATURES --------
st.markdown("## 🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("📸 Food Scan")
    st.write("Upload food packet images and extract nutritional data")

with col2:
    st.info("📦 Barcode Detection")
    st.write("Detect product using barcode and dataset")

with col3:
    st.warning("📊 Health Score")
    st.write("Get smart analysis based on sugar and fat")

st.markdown("---")

# -------- CTA --------
st.markdown("""
<h3 style='text-align:center;'>👉 Start by going to Analyzer from sidebar</h3>
""", unsafe_allow_html=True)

st.markdown("---")

