# Titanic Dataset - Data Cleaning & Preprocessing


## 📌Objective
To learn how to clean and prepare raw data for machine learning using the Titanic dataset.

---

## Dataset
- File used: `Titanic-Dataset.csv`

---

## ✅ Tasks Performed

### 1. Data Loading & Exploration
- Checked data types and missing values using `info()`, `describe()`, and `isnull().sum()`.

### 2. Handling Missing Values
- Filled missing values in:
  - `Age` with **median**
  - `Embarked` with **mode**

### 3. Encoding Categorical Variables
- Applied **one-hot encoding** to `Sex` and `Embarked`.

### 4. Feature Scaling
- Applied **StandardScaler** to:
  - `Age`
  - `Fare`

### 5. Outlier Visualization
- Used **boxplots** to detect outliers in:
  - `Age`
  - `Fare`

---

## Files Included
- `Data_Cleaning_Preprocessing.py` → Python script containing all preprocessing steps
- `Titanic-Dataset.cs` → Dataset
- `Screenshots` → Output

---


##  Key Learnings
- Efficient handling of missing data
- Difference between label and one-hot encoding
- Importance of feature scaling
- Outlier detection techniques using visualization

---

## 📎 How to Run
1. Clone the repo  
2. Install dependencies:  
   `pip install pandas numpy matplotlib seaborn`  
3. Run `Data_Cleaning_Preprocessing.py` or open the notebook  
'''
