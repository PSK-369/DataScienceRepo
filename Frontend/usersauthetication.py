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



warnings.filterwarnings('ignore')

def login_form():
    st.title('User authetication form')
    st.set_page_config(page_title='User access form',layout='centered')
    with st.form(key="inputs",clear_on_submit=True,border=True):
      username=st.text_input(label="Username",label_visibility='visible',help='Enter the username always @gmail.com needs to be present')
      password=st.text_input(label="password",label_visibility='hidden',help="password combination of caps smalls numbers special characters[!@#$^&*]")
      submit= st.form_submit_button(label='submit',type='primary')
      if submit:
          st.info("form is submitting")
          time.sleep(5)
          st.warning("form elements is validating....!")
          response = requests.post(url="http://localhost/username",timeout=10)
          if response.status_code == 200:
              st.info("form is submitted and form validation are completed")
              time.sleep(2)
              st.info("form is redirecting into main page")
              redirect = st.button(label='redirect',type='secondary')
              if redirect:
                st.switch_page("../pages/main.py")
          elif response != 200:
              response.json()
          else:
              response.text()

try:
    login_form()

except Exception as e:
    str.code(traceback.format_exc())
else:
    st.info("no errors in the code")
    
finally:
    st.info("Final block is executed....!")
    st.feedback(options=['stars'])



