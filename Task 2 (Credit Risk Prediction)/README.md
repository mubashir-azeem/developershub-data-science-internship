# Task 4 - Predicting Insurance Claim Amounts

## Objective
The objective of this project is to predict medical insurance charges using machine learning regression techniques based on personal information such as age, BMI, smoking habits, and region.

---

# Dataset Information

Dataset Used:
- Medical Cost Personal Dataset

Features:
- age
- sex
- bmi
- children
- smoker
- region
- charges

Target Variable:
- charges

---

# Technologies Used

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

---

# Steps Performed

## 1. Data Loading
- Loaded dataset using pandas
- Displayed dataset structure using:
  - `.shape`
  - `.columns`
  - `.head()`

## 2. Data Inspection
- Checked dataset information
- Generated statistical summary
- Checked missing values

## 3. Data Visualization
Created:
- BMI vs Charges Scatter Plot
- Age vs Charges Scatter Plot
- Smoking Status vs Charges Box Plot

## 4. Data Preprocessing
- Encoded categorical columns using Label Encoding

## 5. Model Training
- Trained Linear Regression model

## 6. Model Evaluation
Evaluated model using:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

---

# Results

MAE:
- 4186.50

RMSE:
- 5799.58

---

# Key Observations

- Smokers have significantly higher insurance charges.
- Insurance charges increase with age and BMI.
- Smoking status is one of the strongest factors affecting insurance cost.

---

# Conclusion

The project successfully predicted insurance charges using Linear Regression. Different visualization techniques helped identify relationships between personal factors and insurance costs. The model achieved reasonable prediction accuracy using regression techniques.

---

# Author
Mubashir Azeem Abbasi
