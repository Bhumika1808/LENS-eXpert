
import streamlit as st
import joblib
import pandas as pd

review_model=joblib.load("review.pkl")

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
        <span style="color:#283593;">🍽️Food Review Sentiment Analyzer</span>
    </h1>
""", unsafe_allow_html=True)

msg=st.text_input("Enter Review",placeholder="e.g: The ambience was great and the food was delicious!")
if st.button("Analyze",key='al1'):
            pred=review_model.predict([msg])
            if pred[0]==0:
                st.error("The customer gave Negative review 👎")
            else:
                st.success("The customer gave Positive review 👍")
                

st.markdown("#### OR")
uploaded_file = st.file_uploader("Choose a file",type=["csv", "txt"],key='u1')
    
    
if uploaded_file:
                
            df_review=pd.read_csv(uploaded_file,header=None,names=['Msg'])
        
            pred=review_model.predict(df_review.Msg)
            df_review.index=range(1,df_review.shape[0]+1)
            df_review["Prediction"]=pred
            df_review["Prediction"]=df_review["Prediction"].map({0:'Disliked 👎',1:'Liked 👍'})
            st.dataframe(df_review)