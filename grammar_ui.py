import streamlit as st
import requests

st.title("📝 AI Grammar Assistant")
st.write("Enter your text below and get instant grammar corrections!")

user_input = st.text_area("Your text", height=200)

if st.button("Correct Grammar"):
    if user_input.strip() != "":
        response = requests.post(
            "http://127.0.0.1:5000/grammar-check",
            json={"text": user_input}
        )
        result = response.json().get("corrected_text")
        st.success("✅ Corrected Text:")
        st.write(result)
