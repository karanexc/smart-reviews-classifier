import streamlit as st
import joblib

model = joblib.load("models/logistic_model.joblib")
vectorizer = joblib.load("models/tfidf_vectorizer.joblib")

st.title("Amazon Review Sentiment Classifier")

review = st.text_area("Enter your review:")

if st.button("Predict"):
    if review:
        vect = vectorizer.transform([review])
        pred = model.predict(vect)[0]
        label = "Positive" if pred == 0 else "Negative"
        st.success(f"Prediction: {label}")