import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Fake Website Detector")

url = st.text_input("Enter Website URL")

if st.button("Check"):
    data = vectorizer.transform([url])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠ Suspicious Website")
    else:
        st.success("✅ Safe Website")
        