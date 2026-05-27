import streamlit as st
import json

st.set_page_config(page_title="Profile", layout="centered")

st.title("👤 User Profile")

name = st.text_input("Enter your name")
diabetic = st.checkbox("Are you diabetic?")
fitness = st.selectbox("Your goal", ["General", "Weight Loss", "Muscle Gain"])

if st.button("Save Profile"):
    data = {
        "name": name,
        "diabetic": diabetic,
        "goal": fitness
    }

    with open("data/user.json", "w") as f:
        json.dump(data, f)

    st.success("Profile saved!")