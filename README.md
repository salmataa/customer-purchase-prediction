# Customer Purchase Prediction Model

This project uses machine learning to identify high-value repeat customers based on retail transaction data.

## Project Overview
The goal of this project is to help businesses:
- Identify loyal customers
- Predict future purchasing behavior
- Improve customer retention strategies

## Techniques Used
- Data Cleaning & Preprocessing
- Feature Engineering (RFM Analysis)
- Machine Learning Models:
  - Logistic Regression
  - K-Nearest Neighbors (KNN)
- Model Evaluation:
  - ROC Curve
  - Classification Report
  - Accuracy & ROC-AUC

## Results
- ROC-AUC Score: ~0.90
- Strong model performance in predicting high-value customers

## Model Performance

### Logistic Regression
- Accuracy: ~0.87
- ROC-AUC: ~0.91

### K-Nearest Neighbors (KNN)
- Accuracy: ~0.85
- ROC-AUC: ~0.89

The Logistic Regression model performed better overall and was selected as the final model.

## ROC Curve
![ROC Curve](roc_curve.png)

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Dataset
Dataset used: Online Retail Dataset (UCI Machine Learning Repository)

## How to Run
1. Clone the repository
2. Install dependencies:
```
pip install pandas numpy matplotlib scikit-learn openpyxl
```
3. Run:
```
python retail_model.py
```

---

## Business Impact
This model can help companies:
- Target high-value customers
- Personalize marketing strategies
- Increase revenue through retention

---

## Author
Salmata Gueye
