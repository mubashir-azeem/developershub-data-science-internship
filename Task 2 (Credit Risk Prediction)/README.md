# Task 2 - Credit Risk Prediction

## Objective
The objective of this project is to predict whether a loan applicant is likely to get loan approval using machine learning classification techniques.

---

# Dataset Information

Dataset Used:
- Loan Prediction Dataset

Features:
- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

Target Variable:
- Loan_Status

---

# Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# Steps Performed

## 1. Data Loading
- Loaded dataset using pandas
- Displayed first 5 rows using `.head()`

## 2. Data Understanding
- Checked dataset shape
- Displayed column names
- Used `.info()` and `.describe()`

## 3. Data Cleaning
- Checked missing values
- Filled missing categorical values using mode
- Filled missing numerical values using median

## 4. Data Visualization
Created:
- Loan Amount Distribution
- Education vs Loan Status
- Applicant Income Distribution

## 5. Data Preprocessing
- Encoded categorical columns using Label Encoding

## 6. Model Training
- Trained Logistic Regression model

## 7. Model Evaluation
Evaluated model using:
- Accuracy Score
- Confusion Matrix

---

# Results

Accuracy:
- 78%

---

# Key Observations

- Most applicants applied for medium loan amounts.
- Graduates received more loan approvals.
- Income and loan amount affected loan approval status.

---

# Conclusion

The project successfully predicted loan approval using Logistic Regression. Data preprocessing, visualization, and classification techniques were applied effectively. The model achieved good accuracy on testing data.

---

# Author

Mubashir Azeem Abbasi
