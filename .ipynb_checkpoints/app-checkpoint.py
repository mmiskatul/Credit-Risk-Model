import streamlit as st 
import pandas as pd 
import joblib 


model =joblib.load("Decision_tree_credit_model.pkl") 
encoders ={col:joblib.load(f"{col}_encoder.pkl") for col in ["Sex","Housing","Saving accounts","Checking accounts"]} 

st.title("Credit Risk Prediction App") 
st.write("Enter applicant information to predict if the credit risk is good or bad ") 

age =st.number_input("Age",min_value=18,max_value=80,value=30) 
sex =st.selectbox("Sex",["male","Female"]) 

Job =st.number_input("Job (0-3)",min_value=0,max_value=3,value=1) 
housing =st.selectbox("Housing",["Own","Rent","Free"])
saving_account =st.selectbox("Saving Accounts",["little","moderate","rich","quite rich"])
Checking_account =st.selectbox("Checking Accounts",["little","moderate","rich","quite rich"])
credit_amount =st.number_input("Credit Amount",min_value=0,value=1000) 
duration =st.number_input("Duration (month)",min_value=1,value=12) 


input_df =pd.DatFrame({
    "Age":[age],
    "Sex":[encoders["Sex"].transform([sex])[0]], 
    "Job":[Job],
    "Housing":[encoders["Housing"].transform([housing])[0]], 
    "Saving accounts":[encoders["Saving Account"].transform([saving_account])[0]], 
    "Cheking accounts":[encoders["Checking Account"].transform([Checking_account])[0]], 
    "Credit amount":[credit_amount] ,
    "Duration":[duration]
})