import streamlit as st
from PIL import Image
import pytesseract
import re
import cv2
import numpy as np

from backend.history import save_history
from backend.voice import speak
from backend.dataset_lookup import get_product
from backend.barcode import scan_barcode

st.set_page_config(page_title="Analyzer", layout="wide")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# -------- UI --------
st.markdown("""
<h1 style='text-align:center;'>🔍 Food Analyzer</h1>
<p style='text-align:center; color:gray;'>Upload food packet and get smart health insights</p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload Food Packet Image")

# -------- FINAL SMART EXTRACT FUNCTION --------
def extract_value(text, keyword):
    text = text.lower()
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    keyword_map = {
        "fat": ["fat", "total fat", "fats"],
        "sugar": ["sugar", "sugars"]
    }

    keys = keyword_map.get(keyword, [keyword])

    # SAME LINE (number anywhere)
    for line in lines:
        for key in keys:
            if key in line:
                match = re.search(r"([0-9]+\.?[0-9]*)", line)
                if match:
                    return float(match.group(1))

    # NEXT LINE
    for i, line in enumerate(lines):
        for key in keys:
            if key in line and i + 1 < len(lines):
                next_line = lines[i + 1]
                match = re.search(r"([0-9]+\.?[0-9]*)", next_line)
                if match:
                    return float(match.group(1))

    # GLOBAL SEARCH
    for key in keys:
        pattern = rf"{key}[^0-9]*([0-9]+\.?[0-9]*)"
        match = re.search(pattern, text)
        if match:
            return float(match.group(1))

    return None

# -------- MAIN --------
if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, width=280)

    # -------- OCR --------
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(gray)
    text_lower = text.lower()

    # OCR corrections
    text_lower = text_lower.replace("lat", "fat")
    text_lower = text_lower.replace("sugor", "sugar")

    with st.expander("📄 Extracted Text"):
        st.write(text)

    # -------- BARCODE --------
    barcode = scan_barcode(image)
    product_data = None

    if barcode:
        st.success(f"📦 Barcode: {barcode}")
        product_data = get_product(barcode)

    # -------- DATA SOURCE --------
    if product_data:
        st.info(product_data.get("name", "Product"))
        sugar = product_data.get("sugar", 0)
        fat = product_data.get("fat", 0)
    else:
        sugar = extract_value(text_lower, "sugar")
        fat = extract_value(text_lower, "fat")

    # -------- ANALYSIS --------
    st.markdown("## 🧠 AI Analysis")

    score = 10

    c1, c2 = st.columns(2)

    with c1:
        if sugar is not None:
            if sugar > 10:
                st.error(f"Sugar: {sugar}g ❌")
                score -= 3
            else:
                st.success(f"Sugar: {sugar}g")
        else:
            st.warning("Sugar not detected")

    with c2:
        if fat is not None:
            if fat > 10:
                st.error(f"Fat: {fat}g ❌")
                score -= 3
            else:
                st.success(f"Fat: {fat}g")
        else:
            st.warning("Fat not detected")

    # -------- SCORE --------
    st.markdown("## ⭐ Health Score")
    st.progress(score / 10)
    st.markdown(f"<h3 style='color:#00ffae;'>Score: {score}/10</h3>", unsafe_allow_html=True)

    if score >= 8:
        rec = "Healthy"
    elif score >= 5:
        rec = "Moderate"
    else:
        rec = "Unhealthy"

    st.info(rec)

    # -------- SAVE HISTORY --------
    name = product_data["name"] if product_data else "Scanned Product"

    save_history(
        name,
        sugar if sugar else 0,
        fat if fat else 0,
        score
    )

    # -------- VOICE --------
    if st.button("🔊 Speak"):
        speak(rec)