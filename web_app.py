# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:57:09 2022

@author: Admin
"""

import numpy as np
import pickle
import streamlit as st
from flask import Flask, render_template, request
# loading the saved model
with open('./artifacts/alk.pickle', 'rb') as g:
    loaded_model = pickle.load(g)

def insurance_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray ( input_data )

    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape ( 1,-1 )

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return 'The insurance cost is USD', prediction [0]



def main():
    
    
    # giving a title
    st.set_page_config(page_title='Insurance Prediction Web App', page_icon=":tada:", layout="wide")
        # getting the input data om the user

    form= st.form(key="form1")
    form.Age = st.text_input('Age of the Person')
    form.Sex = st.text_input('Sex of the Person')
    form.BMI = st.text_input('BMI value')
    form.Children = st.text_input('No of Children')
    form.Smoker= st.text_input('Is the Person is smoker')
    form.Region = st.text_input('Region of a Person')
    form.form_submit_button("Submit")
    print(form.Age,form.Sex,form.BMI,form.Children)

if __name__ == '__main__':
    main()    
    
    
