import streamlit as st

import joblib
import pandas as pd

try:
    # Use raw string or forward slashes to avoid escape issues
    model1 = joblib.load(
        r"C:\Shravan\PythonPratice\supervised\streamlitapplication\linear_reg.joblib"
    )

    st.title("** Employee Salary Predictions ** ")
    st.write("Model loaded successfully!")
    st.balloons()
    st.sidebar.write("Enter the input details")

    with st.form(key="form-input"):
        with st.sidebar:
            Age = st.number_input("Age", min_value=10, max_value=90, value=24)
            Experience = st.number_input(
                "Experience", min_value=0, max_value=50, value=2
            )  # Fixed max
            Education_encoded = st.number_input(
                "Education_encoded", min_value=0, max_value=3, value=2
            )
            Location_encoded = st.number_input(
                "Location_encoded", min_value=0, max_value=3, value=2
            )
            Gender_encoded = st.number_input(
                "Gender_encoded",
                min_value=1,
                max_value=2,
                value=1,
                help="1 is male and 2 female",
            )
            submit_button = st.form_submit_button(label="Submit")

        if submit_button:
            data1 = {
                "Age": Age,
                "Experience": Experience,
                "Education_encoded": Education_encoded,
                "Location_encoded": Location_encoded,
                "Gender_encoded": Gender_encoded,
            }
            df = pd.DataFrame(data=data1, index=[0])
            prediction = model1.predict(df)
            st.write(f"The predicted salary is: ruppes {prediction[0]:,.2f}")
            st.write("Thank you.....!  :) ")
            st.balloons()

except Exception as e2:
    st.error(f"An error occurred: {e2}")
    st.code(str(e2), language="python")

else:
    st.write("No errors in the code (else block).")

finally:
    st.write("Executed finally block.")
