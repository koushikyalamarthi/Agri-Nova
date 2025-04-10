# 🌾 AgriNova – Smart Farming Assistant

**AgriNova** is a smart farming web application that empowers farmers and agri-enthusiasts with machine learning and deep learning solutions to improve crop productivity, sustainability, and decision-making.

🔗 **Live Demo:** [AgriNova Web App](https://agrinova.streamlit.app/)

---

## 🚀 Features

- **🌱 Plant Disease Detection**  
  Upload a plant leaf image and get instant disease prediction using a Deep Learning model (CNN – ResNet9 architecture).  
  Helps in early diagnosis and prevention.

- **🌾 Crop Recommendation**  
  Based on user inputs like soil type (N, P, K levels), pH, rainfall, temperature, and humidity — a **Random Forest** model predicts the best crop to grow in the given conditions.

- **💊 Fertilizer Suggestion**  
  Uses logic-driven rules to recommend fertilizers based on nutrient deficiencies and crop type.

- **📈 Action Advisory**  
  Provides region-specific agricultural advice by analyzing crop patterns, trends, and simulated weather conditions using a trained machine learning model.

---

## 🧠 Model Architecture & Working

### 🔍 1. **Plant Disease Detection**
- Model: Convolutional Neural Network (ResNet9)
- Framework: PyTorch → Converted to TensorFlow Lite for efficient inference
- Input: Image of crop leaf
- Output: Predicted disease category (e.g., Healthy, Bacterial Blight, Early Blight, etc.)

### 🌾 2. **Crop Recommendation**
- Model: Random Forest Classifier
- Input Features:
  - Nitrogen (N), Phosphorus (P), Potassium (K)
  - Temperature, Humidity
  - pH value, Rainfall
- Output: Recommended crop (e.g., Rice, Wheat, Maize)

### 💊 3. **Fertilizer Suggestion**
- Rule-based logic that:
  - Compares ideal NPK values for a given crop
  - Calculates the deficit/excess
  - Suggests the most suitable fertilizer accordingly

### 📈 4. **Action Advisory**
- Uses a combination of:
  - ML-trained classification model (e.g., Decision Trees or Random Forest)
  - Weather + crop condition trends
- Output: Advisory messages like “Irrigation needed,” “Harvest soon,” etc.

---

## 🛠 Tech Stack

- **Frontend**: Streamlit (Python-based web framework)
- **ML/DL Libraries**: Scikit-learn, TensorFlow, PyTorch, NumPy, Pandas
- **Deployment**: Streamlit Cloud

---

## 📦 Installation & Run Locally

```bash
git clone https://github.com/your-username/agrinova.git
cd agrinova
pip install -r requirements.txt
streamlit run app.py
