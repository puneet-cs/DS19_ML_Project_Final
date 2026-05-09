import streamlit as st
from prediction_helper import predict

st.title("Health insurance Premium Predict")

# create rows with column to receive input
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

categorical_options = {
"gender"  :  ['Male','Female'],
"region"  :  ['Northwest', 'Southeast', 'Northeast' ,'Southwest'],
"bmi_category"  :  ['Normal', 'Obesity' ,'Overweight' ,'Underweight'],
"smoking_status"  :  ['No Smoking', 'Regular' ,'Occasional'],
"employment_status"  :  ['Salaried', 'Self-Employed' ,'Freelancer'],
"insurance_plan"  :  ['Bronze', 'Silver', 'Gold']
}


with row1[0]:
    age = st.number_input('Age', min_value = 18, max_value = 100)
with row1[1]:
    region = st.selectbox("Region", categorical_options["region"] )
with row1[2]:
    number_of_dependants = st.number_input("No. of Dependents", min_value = 0,max_value = 5)

with row2[0]:
    bmi_category = st.selectbox('BMI Category', categorical_options["bmi_category"])
with row2[1]:
    income_lakhs = st.number_input("Income in Lakhs", min_value = 0, max_value = 100)
with row2[2]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options["insurance_plan"])

with row3[0]:
    genetical_risk = st.number_input("Genetic Risk", min_value = 0, max_value = 5)
with row3[1]:
    total_risk_score = st.number_input("total_risk_score", min_value = 0, max_value = 14)
with row3[2]:
    gender_Male = st.selectbox('Gender', categorical_options["gender"])

with row4[0]:
    employment_status = st.selectbox('Employment Status', categorical_options["employment_status"])
with row4[1]:
    smoking_status = st.selectbox('Smoking Status', categorical_options["smoking_status"])

input_dict = {
    'age' : age,
    'region' : region,
    'number_of_dependants' : number_of_dependants,
    'bmi_category' : bmi_category,
    'income_lakhs' : income_lakhs,
    'insurance_plan' : insurance_plan,
    'genetical_risk' : genetical_risk,
    'total_risk_score' : total_risk_score,
    'gender_Male' : gender_Male,
    'employment_status' : employment_status,
    'smoking_status' : smoking_status
}

if st.button('PREDICT'):
    prediction = predict(input_dict)
    st.success(f"Your estimated Premium is this much: {prediction}")