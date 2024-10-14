import numpy as np
import pickle
import streamlit as st


al = pickle.load(open("pipe.pkl","rb"))
st.title("Alzheimer's Disease Prediction.")


SleepQuality = st.number_input('SleepQuality')
CholesterolLDL = st.number_input('CholesterolLDL Level')
CholesterolHDL = st.number_input('CholesterolHDL level')
MMSE = st.number_input('MMSE')
FunctionalAssessment = st.number_input('FunctionalAssessment')
MemoryComplaints = st.number_input('Number of MemoryComplaints')
BehavioralProblems = st.number_input('Number of BehavioralProblems')
ADL = st.number_input('ADL')

if st.button('Alzheimers Test Result'):
    user_input = [[SleepQuality, CholesterolLDL, CholesterolHDL, MMSE,FunctionalAssessment, MemoryComplaints, BehavioralProblems,ADL]]
    prediction = al.predict(user_input)
    if prediction[0] == 1:
        st.success('Positive')
    else:
        st.success('Negative')