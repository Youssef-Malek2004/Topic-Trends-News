import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load trained model and label encoder
pipeline = joblib.load("models/news_classifier.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

st.title("📰 News Category Classifier")

# User input
title = st.text_input("Enter a news title:")

if st.button("Predict"):
    if title:
        # Predict category
        probabilities = pipeline.predict_proba([title])[0]
        categories = label_encoder.classes_
        predicted_label = np.argmax(probabilities)
        predicted_category = categories[predicted_label]

        # Display Prediction
        st.write(f"**Predicted Category:** {predicted_category}")

        # Probability Chart
        fig, ax = plt.subplots()
        ax.bar(categories, probabilities, color="skyblue")
        ax.set_ylabel("Probability")
        ax.set_title("Category Probability Distribution")
        st.pyplot(fig)
