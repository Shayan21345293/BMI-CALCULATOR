# Project 7: BMI Calculator (Streamlit), by SHAYAN ALI

import streamlit as st


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😔"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight ✅"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️"
    else:
        return "Obese ❌"


st.title("💪 BMI Calculator by SHAYAN ALI") 
st.write("Enter your details below to calculate your Body Mass Index (BMI).")

# User input for weight and height
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01, format="%.2f")

if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        st.success(f"**Your BMI is:** {bmi:.2f}")
        st.info(f"**Category:** {category}")
    else:
        st.error("❌ Please enter valid weight and height values.")
