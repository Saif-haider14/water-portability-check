import pickle
import streamlit as st
import numpy as np
# 1. Page Setup
st.set_page_config(page_title="💧 Full Water Potability Predictor", page_icon="💧", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.shutterstock.com/image-photo/stunning-capture-clear-blue-water-600nw-2494172253.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    /* White box for the form inputs */
    div[data-testid="stForm"] {
        background-color: rgba(255, 255, 255, 0.9);  /* white with slight transparency */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Optional: Style number inputs and button */
    input[type="number"] {
        background-color: white;
        color: black;
        border-radius: 8px;
        padding: 6px;
    }

    button[kind="primary"] {
        background-color: #0077b6;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#2 loading training model
with open("my_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

print(loaded_model)

#3 UI
st.title('Water Potability Predictor')
st.write('Enter the parameter values to check')

# input form
with st.form('input form'):
    col1,col2,col3 = st.columns(3)
    with col1:
        ph = st.number_input('ph(0-14)')
        hardness = st.number_input('hardness(mg/l)')
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

# prediction setup
if submitted:
    input_data = np.array([[ph,hardness,solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]])

    prediction = loaded_model.predict(input_data)

    if (prediction[0] == 1):
        st.success('Safe to drink')
    else:
        st.error('Not safe')