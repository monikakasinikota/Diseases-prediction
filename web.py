import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Diseases Outbreak", 
    layout="wide", 
    page_icon="👨‍⚕️"
)

#diabetes_model=pickle.load(open(r"C:\Users\karthik\Diseases predictions\training_models\diabetes_model.sav",'rb'))
#heart_disease_model=pickle.load(open(r"C:\Users\karthik\Diseases predictions\training_models\heart_model.sav",'rb'))
#parkinsons_model=pickle.load(open(r"C:\Users\karthik\Diseases predictions\training_models\parkinsons_model.sav",'rb'))
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))



with st.sidebar:
    selected=option_menu('prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
if selected=="Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of pregnancies')   #cd "C:\Users\karthik\Diseases predictions\training_models"
    with col2:                                                #streamlit_env\Scripts\activate
        Glucose=st.text_input('Glucose level')
    with col3:
        Bloodpressure=st.text_input('Blood Pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thicknesss value')
    with col2:
        Insulin=st.text_input('Insulin value')
    with col3:
        BMI=st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age=st.text_input('Age value')

    diab_diagnosis=''
    if st.button('Diabetes test Result'):
        user_input=[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
    st.success(diab_diagnosis) 



elif selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input('Age value')   #cd "C:\Users\karthik\Diseases predictions\training_models"
    with col2:                                                #streamlit_env\Scripts\activate
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('cp value')
    with col1:
        trestbps=st.text_input('trestbps value')
    with col2:
        chol=st.text_input('chol value')
    with col3:
        fbs=st.text_input('fbs value')
    with col1:
        restecg=st.text_input('restecg value')
    with col2:
        thalach=st.text_input('thalach value')
    with col3:
        exang=st.text_input('exang value')
    with col1:
        oldpeak=st.text_input('old peak value')
    with col2:
        slope=st.text_input('slope value')
    with col3:
        ca=st.text_input('ca value')
    with col1:
        thal=st.text_input('thal value')

    Heart_diagnosis=''
    if st.button('Heart Diseases test Result'):
        user_input=[Age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_prediction=heart_disease_model.predict([user_input])
        if heart_prediction[0]==1:
            Heart_diagnosis='The person is having heart disease'
        else:
            Heart_diagnosis='The person is not having heart disease'
    st.success(Heart_diagnosis) 

elif selected=="Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
        MDVP_RAP = st.text_input('MDVP:RAP')
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        HNR = st.text_input('HNR')
        RPDE = st.text_input('RPDE')
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        MDVP_APQ = st.text_input('MDVP:APQ')
        D2 = st.text_input('D2')
    with col3:
        Jitter_DDP = st.text_input('Jitter:DDP')
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        NHR = st.text_input('NHR')
        DFA = st.text_input('DFA')
        PPE = st.text_input('PPE')
    parkinsons_diagnosis =''
    if st.button("Predict Parkinson's Disease"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, 
        MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, 
        Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, 
        spread2, D2, PPE]
        try:
            user_input = [float(x) if x else 0.0 for x in user_input]  # Convert empty inputs to 0.0
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")
            st.stop()
        prediction = parkinsons_model.predict([user_input])
        if prediction[0] == 1:
            parkinsons_diagnosis = "The person have Parkinson's disease."
        else:
            parkinsons_diagnosis = "The person doesn't have Parkinson's disease."
    st.success(parkinsons_diagnosis)
    

    
    