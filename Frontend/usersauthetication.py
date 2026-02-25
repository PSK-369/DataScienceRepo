import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime
import warnings
import time
import traceback
import joblib
import streamlit as st
import requests
import os


warnings.filterwarnings("ignore")


def login_form():
    st.set_page_config(page_title="User access form", layout="centered")
    st.title("User authetication form")

    with st.form(key="inputs", clear_on_submit=True, border=True):
        username = st.text_input(
            label="Username",
            label_visibility="visible",
            help="Enter the username always @gmail.com needs to be present",
        )
        password = st.text_input(
            label="password",
            label_visibility="visible",
            type="password",
            help="password combination of caps smalls numbers special characters[!@#$^&*]",
        )
        submit = st.form_submit_button(label="submit", type="primary")
        if submit:
            if username == "" or password == "":
                st.error("please enter the input details")
            else:
                st.info("form is submitting")
                time.sleep(2)
                st.warning("form elements is validating....!")
                try:
                    API_URL = os.getenv("BACKURL", "http://localhost:10094")
                    response = requests.post(
                        url=f"{API_URL}/username",
                        timeout=10,
                        json={"username": username, "password": password},
                    )
                    if response.status_code == 200:
                        st.info("form is submitted and form validation are completed")
                        st.balloons()
                        time.sleep(2)
                        st.info("form is redirecting into main page")
                        st.switch_page("pages/main.py")
                    elif response.status_code != 200:
                        error_msg = response.json().get("detail", "login is failed")
                        st.error(f"error is  {error_msg}")
                    else:
                        return response.text()
                except Exception as e1:
                    st.code(str(traceback.format_exc()))
                except requests.exceptions.ConnectionError as m:
                    st.error(
                        f"Connection error backend server is runnning ot not {str(m)}"
                    )


try:
    login_form()

except Exception as e:
    st.code(traceback.format_exc())
else:
    st.info("no errors in the code")

finally:
    st.info("Final block is executed....!")
    st.feedback(options="stars")
