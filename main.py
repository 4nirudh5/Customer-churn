import streamlit as st
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
import pickle
import pandas as pd 
 
pickle_in = open("/Users/anirudh/Desktop/cc/data/model.sav","rb")
model = pickle.load(pickle_in)

def welcome():
    return "Welcome"

def predict(SeniorCitizen,MonthlyCharges,TotalCharges,gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,tenure):
   
    '''
    SeniorCitizen
    MonthlyCharges
    TotalCharges
    gender
    Partner
    Dependents
    PhoneService
    MultipleLines
    InternetService
    OnlineSecurity
    OnlineBackup
    DeviceProtection
    TechSupport
    StreamingTV
    StreamingMovies
    Contract
    PaperlessBilling
    PaymentMethod
    tenure
    '''

  '''
SeniorCitizen,
MonthlyCharges,
TotalCharges,
Churn,
gender_Female,
gender_Male,
Partner_No,
Partner_Yes,
Dependents_No,
Dependents_Yes,
PhoneService_No,
PhoneService_Yes,
MultipleLines_No,
MultipleLines_No,
phone service,
MultipleLines_Yes,
InternetService_DSL,
InternetService_Fiber optic,
InternetService_No,
OnlineSecurity_No,
OnlineSecurity_No internet service,
OnlineSecurity_Yes,
OnlineBackup_No, 
OnlineBackup_No internet service, 
OnlineBackup_Yes,
DeviceProtection_No, 
DeviceProtection_No internet service,   
DeviceProtection_Yes,    
TechSupport_No,  
TechSupport_No internet service,
TechSupport_Yes, 
StreamingTV_No, 
StreamingTV_No internet service,
StreamingTV_Yes, 
StreamingMovies_No,  
StreamingMovies_No internet service,
StreamingMovies_Yes, 
Contract_Month-to-month, 
Contract_One year,   
Contract_Two year,   
PaperlessBilling_No, 
PaperlessBilling_Yes,    
PaymentMethod_Bank transfer (automatic),
PaymentMethod_Credit card (automatic),
PaymentMethod_Electronic check,  
PaymentMethod_Mailed check,
tenure_group_1 - 12, 
tenure_group_13 - 24,    
tenure_group_25-36,    
tenure_group_37-48,    
tenure_group_49-60,    
tenure_group_61-72
   '''


    prediction = model.predict([[SeniorCitizen,MonthlyCharges,TotalCharges,gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,tenure]])
    print(prediction)
    return prediction 

def main():
   st.title("Customer churn")
   SeniorCitizen = st.text_input("SeniorCitizen","type here")
   MonthlyCharges = st.text_input("MonthlyCharges","type here")
   TotalCharges = st.text_input("TotalCharges","type here")
   gender = st.text_input("gender","type here")
   Partner = st.text_input("Partner","type here")
   Dependents = st.text_input("Dependents","type here")
   PhoneService = st.text_input("PhoneService","type here")
   MultipleLines = st.text_input("MultipleLines","type here")
   InternetService = st.text_input("InternetService","type here")
   OnlineSecurity = st.text_input("OnlineSecurity","type here")
   OnlineBackup = st.text_input("OnlineBackup","type here")
   DeviceProtection = st.text_input("DeviceProtection","type here")
   TechSupport = st.text_input("TechSupport","type here")
   StreamingTV = st.text_input("StreamingTV","type here")
   StreamingMovies = st.text_input("StreamingMovies","type here")
   Contract = st.text_input("Contract","type here")
   PaperlessBilling = st.text_input("PaperlessBilling","type here")
   PaymentMethod = st.text_input("PaymentMethod","type here")
   tenure = st.text_input("tenure","type here")    
   results = " "
   if st.button("predict"):
    result = predict(SeniorCitizen,MonthlyCharges,TotalCharges,gender,Partner,Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,tenure)
   st.success("the output is {}".format(result))
   if st.button("about"):
     st.text("lets learn")
     st.text("built with streamlit") 


if __name__ == '__main__':
    main()















