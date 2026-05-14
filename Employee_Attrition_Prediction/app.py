import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and preprocessor
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('preprocessor.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="👔",
    layout="centered"
)

# Title
st.title(" Employee Attrition Predictor")
st.markdown("Predict whether an employee is likely to leave the company.")
st.divider()

# Input form
st.subheader("Enter Employee Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 60, 30)
    monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
    years_at_company = st.slider("Years at Company", 0, 40, 5)
    distance_from_home = st.slider("Distance From Home", 1, 30, 5)
    num_companies_worked = st.slider("Num Companies Worked", 0, 10, 2)

with col2:
    department = st.selectbox("Department",
        ["Sales", "Research & Development", "Human Resources"])
    job_role = st.selectbox("Job Role",
        ["Sales Executive", "Research Scientist",
         "Laboratory Technician", "Manufacturing Director",
         "Healthcare Representative", "Manager",
         "Sales Representative", "Research Director",
         "Human Resources"])
    overtime = st.selectbox("OverTime", ["Yes", "No"])
    marital_status = st.selectbox("Marital Status",
        ["Single", "Married", "Divorced"])
    business_travel = st.selectbox("Business Travel",
        ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])

with col3:
    job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
    work_life_balance = st.slider("Work Life Balance (1-4)", 1, 4, 3)
    environment_satisfaction = st.slider("Environment Satisfaction (1-4)", 1, 4, 3)
    relationship_satisfaction = st.slider("Relationship Satisfaction (1-4)", 1, 4, 3)
    performance_rating = st.slider("Performance Rating (1-4)", 1, 4, 3)

st.divider()

# Predict button
if st.button(" Predict Attrition"):

    dept_map = {"Sales": 2, "Research & Development": 1, "Human Resources": 0}
    role_map = {"Sales Executive": 7, "Research Scientist": 6,
                "Laboratory Technician": 3, "Manufacturing Director": 4,
                "Healthcare Representative": 2, "Manager": 5,
                "Sales Representative": 8, "Research Director": 5,
                "Human Resources": 1}
    overtime_map = {"Yes": 1, "No": 0}
    marital_map = {"Single": 2, "Married": 1, "Divorced": 0}
    travel_map = {"Travel_Rarely": 2, "Travel_Frequently": 1, "Non-Travel": 0}

    input_data = pd.DataFrame([{
        'Age': age,
        'BusinessTravel': travel_map[business_travel],
        'DailyRate': 800,
        'Department': dept_map[department],
        'DistanceFromHome': distance_from_home,
        'Education': 3,
        'EducationField': 2,
        'EnvironmentSatisfaction': environment_satisfaction,
        'Gender': 1,
        'HourlyRate': 65,
        'JobInvolvement': 3,
        'JobLevel': 2,
        'JobRole': role_map[job_role],
        'JobSatisfaction': job_satisfaction,
        'MaritalStatus': marital_map[marital_status],
        'MonthlyIncome': monthly_income,
        'MonthlyRate': 14000,
        'NumCompaniesWorked': num_companies_worked,
        'OverTime': overtime_map[overtime],
        'PercentSalaryHike': 14,
        'PerformanceRating': performance_rating,
        'RelationshipSatisfaction': relationship_satisfaction,
        'StockOptionLevel': 1,
        'TotalWorkingYears': 10,
        'TrainingTimesLastYear': 3,
        'WorkLifeBalance': work_life_balance,
        'YearsAtCompany': years_at_company,
        'YearsInCurrentRole': 4,
        'YearsSinceLastPromotion': 2,
        'YearsWithCurrManager': 4
    }])

    # Scale and predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    # Result
    st.subheader(" Prediction Result")
    if prediction == 1:
        st.error(f" High Attrition Risk — {round(probability*100, 1)}% chance of leaving")
        st.markdown("**Reasons:** Overtime, Low Salary, Low Job Satisfaction")
    else:
        st.success(f"Low Attrition Risk — {round(probability*100, 1)}% chance of leaving")
        st.markdown("**Employee seems stable!**")

    # Progress bar
    st.subheader(" Risk Meter")
    st.progress(int(probability * 100))
    st.caption(f"Attrition Probability: {round(probability*100, 1)}%")