# Task 3 - Insurance Claim Prediction

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
- Checked missing values using `.isnull().sum()`
- Dataset had no missing values

## 4. Data Visualization
Created:
- BMI vs Charges Scatter Plot
- Age vs Charges Scatter Plot
- Smoking Status vs Charges Box Plot

## 5. Data Preprocessing
- Encoded categorical columns using Label Encoding

## 6. Model Training
- Trained Linear Regression model

## 7. Model Evaluation
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
- Smoking status strongly affects medical insurance costs.

---

# Conclusion

The project successfully predicted insurance charges using Linear Regression. Visualization and regression techniques helped understand the relationship between personal factors and insurance costs. The model achieved reasonable prediction accuracy.

---

# Author
Mubashir Azeem Abbasi
