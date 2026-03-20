import streamlit as st

st.title("Welcome to BMI Calculator")

# Sidebar or main page inputs
weight = st.number_input("Enter weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter height (feet)", min_value=0.1, step=0.01)
    
if st.button("Calculate BMI"):
    meter=(height*0.3048)
    bmi = weight / (meter ** 2)
    st.subheader(f"Your BMI: {bmi:.2f}")
    
    if bmi < 18.5:
        st.info("Category: Underweight")
        st.write("**You can maintain good body mass by adding more protein to your food.**")

    elif 18.5 <= bmi < 25:
        st.success("Category: Normal weight")
        st.write("**You have healthy body mass.**")

    elif 25 <= bmi < 30:
        st.warning("Category: Overweight")
        st.write("**You can maintain a good body mass by focusing more protein and fibers.**")
    else:
        st.error("Category: Obese")