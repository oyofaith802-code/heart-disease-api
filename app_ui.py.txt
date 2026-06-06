import streamlit as st
import requests

st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

st.title("❤️ Heart Disease Risk Analyzer")

# Your deployed FastAPI URL (change if needed)
url = "https://heart-disease-api-e3dw.onrender.com/predict"

st.header("Patient Information")

age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])

resting_blood_pressure = st.number_input("Resting Blood Pressure", 50, 300, 130)
cholestoral = st.number_input("Cholesterol", 100, 600, 200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar", [0, 1])

Max_heart_rate = st.number_input("Max Heart Rate", 50, 250, 150)
exercise_induced_angina = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)

chest_pain_type = st.selectbox(
    "Chest Pain Type",
    ["Typical angina", "Atypical angina", "Non-anginal pain"]
)

rest_ecg = st.selectbox(
    "Rest ECG",
    ["Normal", "ST-T wave abnormality"]
)

slope = st.selectbox(
    "Slope",
    ["Flat", "Upsloping"]
)

vessels = st.selectbox(
    "Vessels Colored by Fluoroscopy",
    ["Zero", "One", "Two", "Three"]
)

thalassemia = st.selectbox(
    "Thalassemia",
    ["No", "Normal", "Reversable Defect"]
)


# ===============================
# PREDICTION BUTTON
# ===============================
if st.button("Predict Risk"):

    data = {
        "age": age,
        "sex": sex,
        "resting_blood_pressure": resting_blood_pressure,
        "cholestoral": cholestoral,
        "fasting_blood_sugar": fasting_blood_sugar,
        "Max_heart_rate": Max_heart_rate,
        "exercise_induced_angina": exercise_induced_angina,
        "oldpeak": oldpeak,

        "chest_pain_type_Atypical_angina": 1 if chest_pain_type == "Atypical angina" else 0,
        "chest_pain_type_Non_anginal_pain": 1 if chest_pain_type == "Non-anginal pain" else 0,
        "chest_pain_type_Typical_angina": 1 if chest_pain_type == "Typical angina" else 0,

        "rest_ecg_Normal": 1 if rest_ecg == "Normal" else 0,
        "rest_ecg_ST_T_wave_abnormality": 1 if rest_ecg == "ST-T wave abnormality" else 0,

        "slope_Flat": 1 if slope == "Flat" else 0,
        "slope_Upsloping": 1 if slope == "Upsloping" else 0,

        "vessels_colored_by_flourosopy_One": 1 if vessels == "One" else 0,
        "vessels_colored_by_flourosopy_Two": 1 if vessels == "Two" else 0,
        "vessels_colored_by_flourosopy_Three": 1 if vessels == "Three" else 0,
        "vessels_colored_by_flourosopy_Zero": 1 if vessels == "Zero" else 0,

        "thalassemia_No": 1 if thalassemia == "No" else 0,
        "thalassemia_Normal": 1 if thalassemia == "Normal" else 0,
        "thalassemia_Reversable_Defect": 1 if thalassemia == "Reversable Defect" else 0,
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code == 200:
            result = res.json()

            prediction = result["prediction"]
            risk = result["risk_percentage"]

            st.subheader(f"Risk Score: {risk}%")

            if prediction == 0:
                st.success("Low Risk 😌")
            else:
                st.error("High Risk ⚠️")

        else:
            st.error(f"API Error: {res.text}")

    except Exception as e:
        st.error(f"Request Failed: {e}")