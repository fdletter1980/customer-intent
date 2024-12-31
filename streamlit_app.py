#!/usr/bin/env python
# coding: utf-8

# In[2]:


import xgboost as xgb
import streamlit as st
import pandas as pd
import pickle

#Loading up the Classification model we created
pkl_filename = "stacking_classifier.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

#Caching the model for faster loading
@st.cache


# Define the prediction function
def predict(CityTier, DurationOfPitch, NumberOfPersonVisiting, NumberOfFollowups, PreferredPropertyStar, NumberOfTrips, 
            Passport, PitchSatisfactionScore, OwnCar, NumberOfChildrenVisiting, MonthlyIncome, Age_Adult, Age_Senior,
            TypeofContact_Self_Enquiry, Occupation_Large_Business, Occupation_Salaried, Occupation_Small_Business,
            Gender_Male, ProductPitched_Deluxe, ProductPitched_King, ProductPitched_Standard, ProductPitched_Super_Deluxe,
            MaritalStatus_Married, MaritalStatus_Single, MaritalStatus_Unmarried, Designation_Executive , Designation_Manager,
            Designation_Senior_Manager, Designation_VP):
    
    #if ProductPitched == 'Fair':
    #    ProductPitched = 0
    #elif ProductPitched == 'Good':
    #    ProductPitched = 1
    #elif ProductPitched == 'Very Good':
    #    ProductPitched = 2
    #elif ProductPitched == 'Premium':
    #    ProductPitched = 3
    #elif ProductPitched == 'Ideal':
    #    ProductPitched = 4    

    prediction = pickle_model.predict(pd.DataFrame([[CityTier, DurationOfPitch, NumberOfPersonVisiting, NumberOfFollowups, PreferredPropertyStar, NumberOfTrips, 
            Passport, PitchSatisfactionScore, OwnCar, NumberOfChildrenVisiting, MonthlyIncome, Age_Adult, Age_Senior,
            TypeofContact_Self_Enquiry, Occupation_Large_Business, Occupation_Salaried, Occupation_Small_Business,
            Gender_Male, ProductPitched_Deluxe, ProductPitched_King, ProductPitched_Standard, ProductPitched_Super_Deluxe,
            MaritalStatus_Married, MaritalStatus_Single, MaritalStatus_Unmarried, Designation_Executive , Designation_Manager,
            Designation_Senior_Manager, Designation_VP]], columns=['CityTier', 'DurationOfPitch', 'NumberOfPersonVisiting', 'NumberOfFollowups', 'PreferredPropertyStar', 'NumberOfTrips', 
            'Passport', 'PitchSatisfactionScore','OwnCar', 'NumberOfChildrenVisiting', 'MonthlyIncome', 'Age_Adult', 'Age_Senior',
            'TypeofContact_Self_Enquiry', 'Occupation_Large_Business', 'Occupation_Salaried', 'Occupation_Small_Business',
            'Gender_Male', 'ProductPitched_Deluxe', 'ProductPitched_King', 'ProductPitched_Standard', 'ProductPitched_Super_Deluxe',
            'MaritalStatus_Married', 'MaritalStatus_Single', 'MaritalStatus_Unmarried', 'Designation_Executive' , 'Designation_Manager',
            'Designation_Senior_Manager', 'Designation_VP']))
    return prediction


st.title('Travel Package Purchase Prediction')
st.image("Travel Bag.jpeg")
st.header('Enter the characteristics of the Travel Package:')
CityTier = st.number_input('CityTier:', min_value=0, max_value=10, value=0)
DurationOfPitch = st.number_input('DurationOfPitch:', min_value=0, max_value=10, value=0)
NumberOfPersonVisiting = st.number_input('NumberOfPersonVisiting:', min_value=0, max_value=10, value=0)
NumberOfFollowups = st.number_input('NumberOfFollowups:', min_value=0, max_value=10, value=0)
PreferredPropertyStar = st.number_input('PreferredPropertyStar:', min_value=0, max_value=10, value=0)
NumberOfTrips = st.number_input('NumberOfTrips:', min_value=0, max_value=10, value=0) 
Passport = st.number_input('Passport:', min_value=0, max_value=10, value=0)
PitchSatisfactionScore = st.number_input('PitchSatisfactionScore:', min_value=0, max_value=10, value=0)
OwnCar = st.number_input('OwnCar:', min_value=0, max_value=10, value=0)
NumberOfChildrenVisiting = st.number_input('NumberOfChildrenVisiting:', min_value=0, max_value=10, value=0)
MonthlyIncome = st.number_input('MonthlyIncome:', min_value=0, max_value=10, value=0)
Age_Adult = st.number_input('Age_Adult:', min_value=0, max_value=10, value=0)
Age_Senior = st.number_input('Age_Senior:', min_value=0, max_value=10, value=0)
TypeofContact_Self_Enquiry = st.number_input('TypeofContact_Self_Enquiry:', min_value=0, max_value=10, value=0)
Occupation_Large_Business = st.number_input('Occupation_Large_Business:', min_value=0, max_value=10, value=0)
Occupation_Salaried = st.number_input('Occupation_Salaried:', min_value=0, max_value=10, value=0)
Occupation_Small_Business = st.number_input('Occupation_Small_Business:', min_value=0, max_value=10, value=0)
Gender_Male = st.number_input('Gender_Male:', min_value=0, max_value=10, value=0)
ProductPitched_Deluxe = st.number_input('ProductPitched_Deluxe:', min_value=0, max_value=10, value=0)
ProductPitched_King = st.number_input('ProductPitched_King:', min_value=0, max_value=10, value=0)
ProductPitched_Standard = st.number_input('ProductPitched_Standard:', min_value=0, max_value=10, value=0)
ProductPitched_Super_Deluxe = st.number_input('ProductPitched_Super_Deluxe:', min_value=0, max_value=10, value=0)
MaritalStatus_Married = st.number_input('MaritalStatus_Married:', min_value=0, max_value=10, value=0)
MaritalStatus_Single = st.number_input('MaritalStatus_Single:', min_value=0, max_value=10, value=0)
MaritalStatus_Unmarried = st.number_input('MaritalStatus_Unmarried:', min_value=0, max_value=10, value=0)
Designation_Executive = st.number_input('Designation_Executive:', min_value=0, max_value=10, value=0)
Designation_Manager = st.number_input('Designation_Manager:', min_value=0, max_value=10, value=0)
Designation_Senior_Manager = st.number_input('Designation_Senior_Manager:', min_value=0, max_value=10, value=0)
Designation_VP = st.number_input('Designation_VP:', min_value=0, max_value=10, value=0)

#cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])


if st.button('Predict Price'):
    prediction = predict(CityTier, DurationOfPitch, NumberOfPersonVisiting, NumberOfFollowups, PreferredPropertyStar, NumberOfTrips, 
            Passport, PitchSatisfactionScore, OwnCar, NumberOfChildrenVisiting, MonthlyIncome, Age_Adult, Age_Senior,
            TypeofContact_Self_Enquiry, Occupation_Large_Business, Occupation_Salaried, Occupation_Small_Business,
            Gender_Male, ProductPitched_Deluxe, ProductPitched_King, ProductPitched_Standard, ProductPitched_Super_Deluxe,
            MaritalStatus_Married, MaritalStatus_Single, MaritalStatus_Unmarried, Designation_Executive , Designation_Manager,
            Designation_Senior_Manager, Designation_VP)
    st.success(f'The prediction is {prediction[0]:.2f}')


# In[ ]:




