# 🏠 House Price Prediction using Machine Learning

A complete Machine Learning project that predicts California house prices using multiple regression algorithms and compares their performance.

---

## 📌 Overview

This project demonstrates an end-to-end Machine Learning regression workflow using the California Housing dataset.

The notebook includes:

- Data Loading
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Comparison
- Feature Importance Visualization

---

## 📂 Dataset

California Housing Dataset

Loaded directly from Scikit-learn

```python
from sklearn.datasets import fetch_california_housing
```

Target Variable

- Median House Value

Features

- MedInc
- HouseAge
- AveRooms
- AveBedrms
- Population
- AveOccup
- Latitude
- Longitude

---

## 🤖 Models Used

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

---

## 📊 Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

---

## 🏆 Model Comparison

| Model | MSE | R² Score |
|--------|------|----------|
| Random Forest | 0.253654 | 0.806431 |
| Gradient Boosting | 0.271940 | 0.792477 |
| Linear Regression | 0.555892 | 0.575788 |

Best Performing Model

✅ Random Forest Regressor

---

## 📈 Feature Importance

Random Forest identifies the most important features affecting house prices.

Top Features include:

- Median Income
- Average Rooms
- Latitude
- Longitude
- House Age
---

## 🛠 Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 🚀 Installation

```bash
https://github.com/rranish887-debug/house_price_prediction_machine_learning.git

cd house_price_prediction_machine_learning

pip install -r requirements.txt
```

---

## ▶ Run

```bash
jupyter notebook day19.2.ipynb
```

---

## 📁 Repository Structure

```
house-price-prediction-ml/
│
├── README.md
├── requirements.txt
├── day19.ipynb
├── images/
└── model/
```

---

## 💡 Future Improvements

- Hyperparameter Tuning
- XGBoost
- SHAP Explainability
- Streamlit Dashboard
- Flask API
- Docker Deployment

---

## 👩‍💻 Author

**RANISH A**

AI & Data Science Student
