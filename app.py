from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model & label encoder
pipeline = joblib.load("models/news_classifier.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

# Define FastAPI app
app = FastAPI()


# Define request structure
class NewsTitle(BaseModel):
    title: str


@app.post("/predict/")
def predict_category(data: NewsTitle):
    # Get probability scores for each category
    probabilities = pipeline.predict_proba([data.title])[0]

    # Get category labels
    categories = label_encoder.classes_

    # Get predicted category
    predicted_label = np.argmax(probabilities)
    predicted_category = categories[predicted_label]

    # Format response
    response = {
        "category": predicted_category,
        "probabilities": {cat: float(prob) for cat, prob in zip(categories, probabilities)}
    }

    return response

# Run with: uvicorn app:app --host 0.0.0.0 --port 8000 --reload
