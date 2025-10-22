import streamlit as st
import requests

st.title("Insurance Charges Predictor")

# User Inputs
age = st.number_input("Age", min_value=0, max_value=120)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, format="%.2f")
children = st.selectbox("Children", list(range(0, 16)))
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region", ["Northwest", "Southeast", "Southwest"])

# Map user-friendly inputs to model features
sex_val = 0 if sex == "Male" else 1
smoker_val = 0 if smoker == "No" else 1
region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0
smoker_bmi = smoker_val * bmi

if st.button("Predict"):
    payload = {
        "age": age,
        "sex": sex_val,
        "bmi": bmi,
        "children": children,
        "smoker": smoker_val,
        "region_northwest": region_northwest,
        "region_southeast": region_southeast,
        "region_southwest": region_southwest,
        "smoker_bmi": smoker_bmi
    }
    response = requests.post("http://16.171.161.159:8000/predict", json=payload)
    if response.status_code == 200:
        st.success(f"Predicted Charge: {response.json()['predicted_charge']}")
    else:
        st.error("Prediction failed. Check input or server.")

