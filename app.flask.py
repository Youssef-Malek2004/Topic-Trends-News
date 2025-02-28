from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import io
import base64

# Load trained model and label encoder
pipeline = joblib.load("models/news_classifier.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")

app = Flask(__name__)

# Function to generate probability plot
def plot_probabilities(probabilities, categories):
    plt.figure(figsize=(6, 4))
    plt.bar(categories, probabilities, color="skyblue")
    plt.xlabel("Category")
    plt.ylabel("Probability")
    plt.title("Category Probability Distribution")
    plt.ylim(0, 1)

    # Convert plot to image
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode("utf-8")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    plot_url = None

    if request.method == "POST":
        title = request.form["title"]
        probabilities = pipeline.predict_proba([title])[0]
        categories = label_encoder.classes_

        # Get predicted category
        predicted_label = np.argmax(probabilities)
        predicted_category = categories[predicted_label]

        # Generate probability distribution chart
        plot_url = plot_probabilities(probabilities, categories)

        prediction = {
            "category": predicted_category,
            "probabilities": dict(zip(categories, probabilities))
        }

    return render_template("index.html", prediction=prediction, plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
