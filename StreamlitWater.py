import pickle
import streamlit as st
import numpy as np

# 1. Page Setup
st.set_page_config(page_title="💧 Full Water Potability Predictor", page_icon="💧", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #a1c4fd, #c2e9fb);
        color: #000000;
    }

    /* Form container */
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Number input boxes */
    input[type="number"] {
        background-color: #f0f9ff;
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 8px;
        font-size: 16px;
        width: 100%;
    }

    /* Button styling */
    button[kind="primary"] {
        background-color: #0077b6;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Load model
with open("my_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# 3. UI
st.title('💧 Water Potability Predictor')
st.write('Enter the parameter values to check:')

# Input form
with st.form('input form'):
    col1, col2, col3 = st.columns(3)
    with col1:
        ph = st.number_input('pH (0-14)')
        hardness = st.number_input('Hardness (mg/L)')
        solids = st.number_input("Solids (ppm)", 0.0)
    with col2:
        chloramines = st.number_input("Chloramines (ppm)", 0.0)
        sulfate = st.number_input("Sulfate (mg/L)", 0.0)
        conductivity = st.number_input("Conductivity (μS/cm)", 0.0)
    with col3:
        organic_carbon = st.number_input("Organic Carbon (ppm)", 0.0)
        trihalomethanes = st.number_input("Trihalomethanes (μg/L)", 0.0)
        turbidity = st.number_input("Turbidity (NTU)", 0.0)

    submitted = st.form_submit_button("🔍 Predict")

# Prediction
# Combine ML prediction with pH logic
if submitted:
    input_data = np.array([[ph,hardness,solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]])

    prediction = loaded_model.predict(input_data)

    if (prediction[0] == 1):
        st.success('Safe to drink')
    else:
        st.error('Not safe')
