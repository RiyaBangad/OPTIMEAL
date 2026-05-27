import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

# -------- CUSTOM CSS --------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #e0f7fa, #e8f5e9);
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #2E8B57;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: gray;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------- HERO --------
st.markdown('<div class="title">🍏 Opti-Meal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Powered Food Intelligence</div>', unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; font-size:18px; color:gray;'>
Scan your food. Understand your health. Make smarter choices.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# -------- CARDS --------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📸 Scan Food</h3>
        <p>Upload food packets and extract hidden nutrition details using OCR</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🧠 Smart Analysis</h3>
        <p>Detect sugar, fat, additives and harmful ingredients</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Health Score</h3>
        <p>Get intelligent scoring with real-time health insights</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------- EXTRA FEATURES --------
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <h4>📦 Barcode Scan</h4>
        <p>Instant product detection</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h4>📈 History</h4>
        <p>Track your eating patterns</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <h4>🎤 Voice AI</h4>
        <p>App explains results to you</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -------- CTA --------
st.markdown("""
<h2 style='text-align:center;'>🚀 Ready to analyze?</h2>
<p style='text-align:center;'>Go to Analyzer from sidebar</p>
""", unsafe_allow_html=True)

st.markdown("---")

st.caption("Opti-Meal • Built with ❤️ using AI")