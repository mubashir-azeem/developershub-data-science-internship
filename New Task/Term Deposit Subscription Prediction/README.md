# Task 1 - Term Deposit Subscription Prediction (Bank Marketing Dataset)

## Objective

The objective of this task is to predict whether a bank customer will subscribe to a term deposit using customer demographic information, financial details, and marketing campaign data. The project also aims to compare machine learning models and explain predictions using SHAP (Explainable AI).

---

# Dataset Information

Dataset Used:

* Bank Marketing Dataset (UCI Machine Learning Repository)

Features:

* age
* job
* marital
* education
* default
* balance
* housing
* loan
* contact
* day
* month
* duration
* campaign
* pdays
* previous
* poutcome
* y (Target Variable)

Target Variable:

* yes = Customer subscribed to a term deposit
* no = Customer did not subscribe

Total Records:

* 45,211 rows
* 17 columns

---

# Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* SHAP

---

# Steps Performed

## 1. Data Loading

* Loaded the Bank Marketing dataset
* Displayed dataset structure using:

  * `.shape`
  * `.columns`
  * `.head()`
  * `.info()`

## 2. Data Inspection

* Checked dataset information
* Generated statistical summary
* Checked missing values
* Analyzed categorical feature distributions

## 3. Exploratory Data Analysis (EDA)

Created:

* Target Variable Distribution
* Age Distribution
* Account Balance Distribution
* Job Distribution
* Subscription by Job
* Housing Loan vs Subscription
* Education vs Subscription

## 4. Data Preprocessing

* Encoded target variable
* Applied One-Hot Encoding to categorical features
* Split dataset into training and testing sets

## 5. Model Building

### Logistic Regression

* Trained Logistic Regression model
* Generated predictions
* Evaluated model performance

### Random Forest

* Trained Random Forest Classifier
* Generated predictions
* Evaluated model performance
* Extracted feature importance

## 6. Model Evaluation

Evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC Curve
* ROC-AUC Score

## 7. Explainable AI (SHAP)

Created:

* SHAP Summary Plot
* SHAP Feature Importance Plot
* Individual Customer Prediction Explanations

---

# Model Performance

## Logistic Regression

* Accuracy: 90.07%
* Precision: 64.49%
* Recall: 33.65%
* F1-Score: 44.22%
* ROC-AUC: 0.903

## Random Forest

* Accuracy: 90.59%
* Precision: 66.67%
* Recall: 39.13%
* F1-Score: 49.32%
* ROC-AUC: 0.929

---

# Key Observations

* The dataset is highly imbalanced, with most customers not subscribing to term deposits.
* Call duration was the most important factor affecting subscription predictions.
* Customers with higher account balances showed a greater likelihood of subscribing.
* Customers without housing loans were more likely to subscribe.
* Previous successful marketing campaigns positively influenced future subscriptions.
* Random Forest performed better than Logistic Regression across all evaluation metrics.
* SHAP analysis helped explain individual customer predictions and feature impacts.

---

# Conclusion

The Bank Marketing dataset was successfully analyzed and modeled using machine learning techniques. Two classification models were developed and compared, with Random Forest achieving the best overall performance. SHAP Explainable AI was used to understand the factors influencing model predictions. The final model can help banks identify customers who are more likely to subscribe to term deposits, improving marketing efficiency and decision-making.

---

# Output Visualizations

## Exploratory Data Analysis

* Target Distribution
* Age Distribution
* Balance Distribution
* Job Distribution
* Housing Loan vs Subscription
* Education vs Subscription

## Model Evaluation

* Confusion Matrix
* ROC Curve
* Feature Importance Plot

## Explainable AI

* SHAP Summary Plot
* SHAP Feature Importance Plot
* Customer-Level SHAP Explanations

---

# Author

Mubashir Azeem Abbasi
