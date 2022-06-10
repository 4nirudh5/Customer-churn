import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
	st.title('Welcome')


with dataset:
	st.header('Customer churn dataset')
	st.text('data set from kaggle')

    df = pd.read_csv('data/customer_churn.csv')
    st.write(df.head())

    total_purchase = pd.DataFrame(df['Total_Purchase'].value_counts()).head()
    st.bar_chart(total_purchase)

with features:
    st.header('The features for the model')
 

with model_training:
    st.header('Model training') 
    st.text('choose hyper parameters to see how they perform')    	
