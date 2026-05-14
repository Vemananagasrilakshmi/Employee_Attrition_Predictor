# 👔 Employee Attrition Predictor

## 📌 About
A Machine Learning web app that predicts whether
an employee will leave the company before they
actually resign — helping HR teams take proactive
action and save recruitment costs.

## 📊 Dataset
- **Name:** IBM HR Analytics Dataset
- **Records:** 1470 employees
- **Features:** 35 columns
- **Target:** Attrition (Yes/No)
- **Source:** Kaggle

## 🔄 What We Did

### Step 1 — Exploratory Data Analysis (EDA)
- Analyzed attrition distribution
- Found only 16% employees leave (class imbalance!)
- Discovered younger employees leave more
- Found Sales department has highest attrition
- Overtime employees leave 3x more
- Low salary employees leave more
- Plotted 9 visualizations for deep insights

### Step 2 — Data Preprocessing
- Dropped irrelevant columns
  (EmployeeCount, EmployeeNumber, Over18, StandardHours)
- Encoded target variable (Yes=1, No=0)
- Applied Label Encoding to categorical columns

### Step 3 — Train Test Split
- Split data 80% train / 20% test
- Train: 1176 records
- Test: 294 records

### Step 4 — Handle Class Imbalance (SMOTE)
- Before SMOTE: Stay=978, Leave=198 (Imbalanced!)
- After SMOTE:  Stay=978, Leave=978 (Balanced! ✅)

### Step 5 — Feature Scaling
- Applied StandardScaler
- Scaled all features to same range

### Step 6 — Model Training (6 Algorithms)
- Trained 6 ML algorithms
- Compared Accuracy, Precision, Recall, F1 Score
- Selected best model based on F1 Score

### Step 7 — Deployment
- Built Streamlit web app
- User enters employee details
- App predicts attrition risk in real-time

## 🤖 Algorithms Used
| # | Algorithm | Accuracy | F1 Score |
|---|-----------|----------|----------|
| 1 | Logistic Regression | 80.61% | 42.42% 🏆 |
| 2 | Decision Tree | 82.00% | 40.00% |
| 3 | Random Forest | 86.73% | 40.00% |
| 4 | SVM | 85.37% | 35.82% |
| 5 | KNN | 83.00% | 37.00% |
| 6 | XGBoost | 85.71% | 40.00% |

## 🏆 Best Model
**Logistic Regression** — Highest F1 Score (42.42%)

> Why F1 Score? Dataset is imbalanced (84% vs 16%)
> F1 Score is best metric for imbalanced datasets!

## 🌐 Web App Features
- Enter employee details (Age, Salary, OverTime etc.)
- Get real-time attrition prediction
- See risk percentage (0-100%)
- High Risk ⚠️ or Low Risk ✅ result
- Visual risk meter

## 🛠️ Tech Stack
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- XGBoost
- SMOTE (imbalanced-learn)
- Streamlit

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
