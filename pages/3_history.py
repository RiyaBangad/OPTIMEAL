import streamlit as st
import matplotlib.pyplot as plt

from backend.history import load_history

st.set_page_config(page_title="History", layout="wide")

st.title("📊 Food History")

# -------- LOAD DATA --------
df = load_history()

if df.empty:
    st.warning("No history data available")
    st.stop()

# -------- FIX COLUMN NAMES --------
df.columns = df.columns.str.strip()

# -------- AUTO DETECT COLUMNS --------
sugar_col = None
fat_col = None
score_col = None

for col in df.columns:
    if "sugar" in col.lower():
        sugar_col = col
    if "fat" in col.lower():
        fat_col = col
    if "score" in col.lower():
        score_col = col

# -------- TABLE --------
st.subheader("📋 Recent Data")
st.dataframe(df.tail(10), use_container_width=True)

st.markdown("---")

# -------- GRAPH FUNCTION --------
def plot_graph(data, title):
    fig, ax = plt.subplots(figsize=(3,2))
    ax.plot(data.tail(10))
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# -------- GRAPHS --------
st.subheader("📈 Trends")

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("Sugar Trend")
    if sugar_col:
        plot_graph(df[sugar_col], "Sugar")
    else:
        st.warning("Sugar column not found")

with col2:
    st.caption("Fat Trend")
    if fat_col:
        plot_graph(df[fat_col], "Fat")
    else:
        st.warning("Fat column not found")

with col3:
    st.caption("Score Trend")
    if score_col:
        plot_graph(df[score_col], "Score")
    else:
        st.warning("Score column not found")