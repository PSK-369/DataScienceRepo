import traceback
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime
import warnings
import joblib
import streamlit as st
import time
import seaborn as sns
import os

warnings.filterwarnings("ignore")


try:
    st.set_page_config(page_title="Main Predication Page", layout="centered")
    st.title("Marriage Type predication")
    st.write("------------------")
    st.code(
        f"Models are used ones [Logistic + Decision Tree + Random Forest \n + KNN Classifier + SVC]"
    )

    current_dir = os.path.dirname(os.path.abspath(__file__))
    st.info(current_dir)
    model1 = joblib.load(os.path.join(current_dir, "Logistic_regression.joblib"))
    model2 = joblib.load(os.path.join(current_dir, "Decision_tree.joblib"))
    model3 = joblib.load(os.path.join(current_dir, "Random_forest.joblib"))
    model4 = joblib.load(os.path.join(current_dir, "knn_classifier.joblib"))
    model5 = joblib.load(os.path.join(current_dir, "svc_classifier.joblib"))
    st.info("models are loaded successfully")
    st.divider()
    st.balloons()
    with st.form(key="inputs", clear_on_submit=True):
        with st.sidebar:
            st.header("Choose the Input parameters")
            Age_at_Marriage = st.number_input(
                label="Marraige Age",
                min_value=20,
                max_value=50,
                help="only numericals",
            )
            Children_Count = st.number_input(
                label="childern couns ",
                min_value=0,
                max_value=10,
                help="only numricals",
            )
            Years_Since_Marriage = st.number_input(
                label="years since marriage",
                min_value=1,
                max_value=50,
                help="only numericals",
            )
            Gender_encoded = st.number_input(
                label="Gender",
                min_value=1,
                max_value=2,
                help="('Female', 0), (('Male', 1)",
            )
            Education_Level_encoded = st.number_input(
                label="Education Level",
                min_value=0,
                max_value=3,
                help="""('Graduate', 0),
           ('School', 3),
           ('Postgraduate', 2),
            ('PhD', 1) """,
            )
            Caste_Match_encoded = st.number_input(
                label="caste match",
                min_value=0,
                max_value=1,
                help="""
           dict_keys([('Same', 1), ('Different', 0)])""",
            )
            Religion_encoded = st.number_input(
                label="Religion",
                min_value=0,
                max_value=4,
                help="""
        dict_keys([('Hindu', 1), ('Muslim', 2), ('Christian', 0), ('Others', 3), ('Sikh', 4)])                     
       """,
            )
            Parental_Approval_encoded = st.number_input(
                label="Parent Approval",
                min_value=0,
                max_value=2,
                help="""
           dict_keys([('Yes', 2), ('Partial', 1), ('No', 0)])
           """,
            )
            Urban_Rural_encoded = st.number_input(
                label="Urban and Rural",
                min_value=0,
                max_value=1,
                help="""
           dict_keys([('Urban', 0), ('rural', 1)])
           """,
            )
            Dowry_Exchanged_encoded = st.number_input(
                label="Dowry Excahnge",
                min_value=0,
                max_value=2,
                help="""
           No 0 , Yes 2 , Not diclosed 1
           """,
            )
            Marital_Satisfaction_encoded = st.number_input(
                label="Martial Satisfaction",
                min_value=0,
                max_value=2,
                help="""
           Medium 2 , High 0 , Low 1
           """,
            )
            Divorce_Status_encoded = st.number_input(
                label="Divorce status",
                min_value=0,
                max_value=1,
                help="""
           No 0 , Yes 1
           """,
            )
            Income_Level_encoded = st.number_input(
                label="Income Level",
                min_value=0,
                max_value=2,
                help="""
           High 0, Low 1 and Middle 2
           """,
            )
            Spouse_Working_encoded = st.number_input(
                label="Spouse Working",
                min_value=0,
                max_value=1,
                help="""
           Yes 1 and No  0
           """,
            )
            Inter_Caste_encoded = st.number_input(
                label=" Inter Caste",
                min_value=0,
                max_value=1,
                help="""
          NO 0 and Yes 1
           """,
            )
            Inter_Religion_encoded = st.number_input(
                label="Inter Religion",
                min_value=0,
                max_value=1,
                help="""
           No 0 and Yes 1
           """,
            )
            model_selction = st.selectbox(
                label="Choose the models",
                options=[
                    "ALL",
                    "Logistic",
                    "Decision",
                    "Random",
                    "KNN",
                    "SVC",
                    "RandomModel",
                ],
            )
            # model1 = joblib.load("../ModelsJobs/Logistic_regression.joblib")
            # model2 = joblib.load("../ModelsJobs/Decison_tree.joblib")
            # model3 = joblib.load("../ModelsJobs/Random_forest.joblib")
            # model4 = joblib.load("../ModelsJobs/knn_classifier.joblib")
            # model5 = joblib.load("../ModelsJobs/svc_classifier.joblib")
            submit = st.form_submit_button(
                label="Submit", help="Submit button", type="primary"
            )
            st.write("----------------------")
            try:
                if submit:
                    st.warning("Form is submitting")
                    time.sleep(2)
                    st.info("Fom is submitted")
                    st
                else:
                    st.error("form is not submitted")
            except Exception as e1:
                st.code(str(e1))
    model_dict1 = {
        "Age_at_Marriage": Age_at_Marriage,
        "Children_Count": Children_Count,
        "Years_Since_Marriage": Years_Since_Marriage,
        "Gender_encoded": Gender_encoded,
        "Education_Level_encoded": Education_Level_encoded,
        "Caste_Match_encoded": Caste_Match_encoded,
        "Religion_encoded": Religion_encoded,
        "Parental_Approval_encoded": Parental_Approval_encoded,
        "Urban_Rural_encoded": Urban_Rural_encoded,
        "Dowry_Exchanged_encoded": Dowry_Exchanged_encoded,
        "Marital_Satisfaction_encoded": Marital_Satisfaction_encoded,
        "Divorce_Status_encoded": Divorce_Status_encoded,
        "Income_Level_encoded": Income_Level_encoded,
        "Spouse_Working_encoded": Spouse_Working_encoded,
        "Inter_Caste_encoded": Inter_Caste_encoded,
        "Inter_Religion_encoded": Inter_Religion_encoded,
    }
    # model1 = joblib.load("../ModelsJobs/Logistic_regression.joblib")
    # model2 = joblib.load("../ModelsJobs/Decison_tree.joblib")
    # model3 = joblib.load("../ModelsJobs/Random_forest.joblib")
    # model4 = joblib.load("../ModelsJobs/knn_classifier.joblib")
    # model5 = joblib.load("../ModelsJobs/svc_classifier.joblib")
    df1 = pd.DataFrame(data=model_dict1, index=[0])
    st.code("('Arranged', 0) ---- ('Love', 1)")
    if model_selction == "ALL":
        y_pred1 = model1.predict(df1)
        y_pred2 = model2.predict(df1)
        y_pred3 = model3.predict(df1)
        y_pred4 = model4.predict(df1)
        y_pred5 = model5.predict(df1)
        st.code(
            f"""
            Model name is {model_selction}
            
            Logistic : +++++++++> {abs(y_pred1[0])}
            Decison : +++++++++> {abs(y_pred2[0])}
            Random : +++++++++> {abs(y_pred3[0])} 
            KNN : +++++++++> {abs(y_pred4[0])} 
            SVC : ++++++++++> {abs(y_pred5[0])}
                """
        )
        # ["ALL", "Logistic", "Decision", "Random", "KNN", "SVC"]
    elif model_selction == "Logistic":
        y_pred1 = model1.predict(df1)
        st.code(f"{model_selction} --- result is  +++++++++> {abs(y_pred1[0])}")
    elif model_selction == "Decision":
        y_pred2 = model2.predict(df1)
        st.code(f"{model_selction} --- result is  +++++++++> {abs(y_pred2[0])}")
    elif model_selction == "Random":
        y_pred3 = model3.predict(df1)
        st.code(f"{model_selction} --- result is   +++++++++> {abs(y_pred3[0])}")
    elif model_selction == "KNN":
        y_pred4 = model4.predict(df1)
        st.code(f"{model_selction} --- result is  +++++++++> {abs(y_pred4[0])}")
    elif model_selction == "SVC":
        y_pred5 = model5.predict(df1)
        st.code(f"{model_selction} --- result is  +++++++++> {abs(y_pred5[0])}")
    else:
        if model_selction == "RandomModel":
            y_pred_choice = model2.predict(df1)
            st.code(
                f"{model_selction} --- result is  +++++++++> {abs(y_pred_choice[0])}"
            )
    st.write("-------------------------")
    st.header("Input features in terms of table format")
    st.data_editor(df1)
    st.dataframe(df1)
    st.write("------------------------")
    st.header("Charts Details")

    # col1, col2 = st.columns(2, border=True)
    # with col1:
    cl1 = ["#ff4d01", "#000000"]

    fig1, ax1 = plt.subplots(1, 2, figsize=(8, 5))
    df1.T.plot(kind="barh", ax=ax1[0], color=cl1[1])
    plt.grid(True)
    df1.T.plot(kind="kde", ax=ax1[1], color=cl1[1])
    plt.grid(True)

    st.pyplot(fig1)


except Exception as e:
    st.code(str(e), language="text")
    st.code(traceback.format_exc())
else:
    st.info("No errors inf the code")
    st.header("Logistic + Random + Decison + KNN + SVC")
finally:
    st.write("---------------------------------")
    st.header("Thank You")
    st.feedback("stars")
