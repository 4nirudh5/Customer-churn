import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64 

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('Customer churn prediction :')  
    st.image('/Users/anirudh/Desktop/cc/Elements/cci.png')
    st.
    st.markdown('Applicant Income VS Loan Amount ')
    st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))
