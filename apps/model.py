import streamlit as st
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
import pickle
import pandas as pd 


def app():
    # loading the saved model
    loaded_model = pickle.load(open('model.sav', 'rb'))


    # creating a function for Prediction

    def churn_prediction(input_data):

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
  
        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
           return 'The customer is churned'
        else:
           return 'The customer is not churned'


    def main():

        # giving a title
        st.title('Customer churn Web App')

        # getting the input data from the user

    gender = st.text_input('gender')
    SeniorCitizen = st.text_input('Senior citizen')
    Partner = st.text_input('Partner')
    Dependents = st.text_input('Dependents')
    tenure = st.text_input('tenure')
    PhoneService = st.text_input('PhoneService')
    MultipleLines = st.text_input('MultipleLines')
    OnlineSecurity = st.text_input('OnlineSecurity')
    OnlineBackup= st.text_input('OnlineBackup')
    DeviceProtection = st.text_input('DeviceProtection')
    TechSupport = st.text_input('TechSupport')
    StreamingMovies = st.text_input('StreamingMovies')
    PaperlessBilling = st.text_input('PaperlessBilling')
    MonthlyCharges = st.text_input('MonthlyCharges')
    TotalCharges = st.text_input('TotalCharges')
    
    no_internet_service = st.text_input('no_internet_service')
    StreamingTV = st.text_input('StreamingTV')
    InternetService_DSL = st.text_input('InternetService_DSL')
    InternetService_Fiber_optic = st.text_input('InternetService_Fiber_optic')
    InternetService_No = st.text_input('InternetService_No')
    Contract_Month_to_month = st.text_input('Contract_Month_to_month')
    Contract_One_year = st.text_input('Contract_One_year')
    Contract_Two_year = st.text_input('Contract_Two_year')
    PaymentMethod_Bank_transfer_automatic = st.text_input('PaymentMethod_Bank_transfer_automatic')
    PaymentMethod_Credit_card_automatic = st.text_input('PaymentMethod_Credit_card_automatic')
    PaymentMethod_Electronic_check = st.text_input('PaymentMethod_Electronic_check')
    PaymentMethod_Mailed_check = st.text_input('PaymentMethod_Mailed_check')


    # code for Prediction
    customer_churn = ''

    # creating a button for Prediction

    if st.button('Get churn Test Result'):
      customer_churn = churn_prediction(
        [gender, SeniorCitizen, Partner, Dependents, tenure,
         PhoneService, MultipleLines, OnlineSecurity, OnlineBackup,
         DeviceProtection, TechSupport, StreamingMovies,
         PaperlessBilling, MonthlyCharges, TotalCharges,
         no_internet_service, StreamingTV, InternetService_DSL,
         InternetService_Fiber_optic, InternetService_No,
         Contract_Month_to_month, Contract_One_year,
         Contract_Two_year, PaymentMethod_Bank_transfer_automatic,
         PaymentMethod_Credit_card_automatic,
         PaymentMethod_Electronic_check, PaymentMethod_Mailed_check])

    st.success(customer_churn)


if __name__ == '__main__':
    main()

       
    






