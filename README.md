# **📰 AI-Powered News Category Classifier**  

## **🚀 Overview**  
This project is an **AI-powered news classification system** that allows users to **input a news headline** and receive a **predicted category** along with **probability scores** for all possible categories. It is built using **Flask, Streamlit, and FastAI** to provide a seamless user experience with both a traditional web UI and an interactive dashboard.

---

## **🔹 Features**  
✅ **Flask Web App** – A structured, full-stack web interface for classification.  
✅ **Streamlit Interactive UI** – A lightweight, interactive dashboard for real-time predictions.  
✅ **FastAI Model Integration** – Leverages **FastAI** for efficient and accurate text classification.  
✅ **Category Probability Visualization** – Displays confidence scores in a **bar chart**.  
✅ **API Support** – Provides a RESTful API to integrate with other applications.  

---

## **🛠 Tech Stack**  
- **Backend:** Flask (Python)  
- **Interactive UI:** Streamlit  
- **Machine Learning:** FastAI, Scikit-Learn, XGBoost  
- **Data Processing:** TF-IDF, PCA, StandardScaler  
- **Visualization:** Matplotlib  

---

## **📌 How It Works**  
1️⃣ **User enters a news title** in the UI (Flask or Streamlit).  
2️⃣ **The model processes the text**, extracting meaningful features using TF-IDF.  
3️⃣ **FastAI/XGBoost predicts the category**, returning the top prediction and probability scores.  
4️⃣ **Results are displayed visually**, with probabilities shown in a **bar chart**.  

---

## **🚀 Setup & Installation**  

### **🔹 1. Clone the Repository**  
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/news-classifier.git
cd news-classifier
```

### **🔹 2. Install Dependencies**  
Ensure you have Python **3.8+** installed, then run:  
```bash
pip install -r requirements.txt
```

### **🔹 3. Run the Flask Web App**  
```bash
python app.py
```
Open **http://127.0.0.1:5000/** in your browser.

### **🔹 4. Run the Streamlit Dashboard**  
```bash
streamlit run streamlit_app.py
```
Open **http://localhost:8501/** in your browser.

---

## **📡 API Usage (FastAPI)**
You can also make predictions via an API using FastAPI.

### **🔹 Start the API**
```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

### **🔹 Example API Request**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{"title": "Stock market crashes due to inflation"}'
```

### **🔹 Example API Response**
```json
{
    "category": "business",
    "probabilities": {
        "business": 0.78,
        "entertainment": 0.12,
        "sports": 0.07,
        "technology": 0.03
    }
}
```

---

## **📊 Screenshots**
### **Flask Web Interface**
<img src="screenshots/flask_ui.png" width="600">

### **Streamlit Interactive Dashboard**
<img src="screenshots/streamlit_ui.png" width="600">

### **Category Probability Visualization**
<img src="screenshots/probability_chart.png" width="600">

---

## **🛠 Future Enhancements**  
🔹 Improve **FastAI model performance** with hyperparameter tuning.  
🔹 Deploy on **AWS, Azure, or GCP** for production.  
🔹 Add **support for multilingual news classification**.  
🔹 Implement **real-time news trend analysis**.  

---

## **📜 License**  
This project is licensed under the **MIT License**. Feel free to modify and use it for your own purposes.  

---

## **🤝 Contributing**  
Pull requests are welcome! If you’d like to contribute, please **fork** the repository and submit a PR.  

---

### **💡 Star ⭐ this repo if you find it useful!**  
Happy Coding! 🚀
