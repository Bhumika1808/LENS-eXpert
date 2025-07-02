import streamlit as st
import joblib
import pandas as pd

spam_model=joblib.load("spam_classifier.pkl")

st.markdown(
    """
    <style>
    /* 🌈 Gradient background for the whole app */
    .stApp {
        background: linear-gradient(135deg, #d3f5f8, #e1bee7);
        background-attachment: fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #8a2be2;
        color: white;
    }

    /* Sidebar content */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Optional: Sidebar layout spacing */
    [data-testid="stSidebar"] > div:first-child {
        padding: 20px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <h1 style="font-family:sans-serif;">
        <span style="color:#283593;">🤖Spam Message Detector</span>
    </h1>
""", unsafe_allow_html=True)

msg=st.text_input("Enter Msg", placeholder="e.g: Click here to receive a free car!")
if st.button("Classify",key='cl1'):
            pred=spam_model.predict([msg])
            if pred[0]==0:
                st.error("This is a Spam Msg 🚫")
            else:
                st.success("This is Not a Spam Msg 👍")

st.markdown("#### OR")

uploaded_file = st.file_uploader("Choose a file",type=["csv", "txt"],key='u2')
    
if uploaded_file:
                
            df_spam=pd.read_csv(uploaded_file,header=None,names=['Msg'])
        
            pred=spam_model.predict(df_spam.Msg)
            df_spam.index=range(1,df_spam.shape[0]+1)
            df_spam["Prediction"]=pred
            df_spam["Prediction"]=df_spam["Prediction"].map({0:'Spam Msg 🚫',1:'Not a Spam Msg 👍'})
            st.dataframe(df_spam)