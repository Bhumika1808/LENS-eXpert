import streamlit as st
import joblib
import pandas as pd

language_model=joblib.load("lang_det.pkl")

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
        <span style="color:#283593;">🌐Language Detector</span>
    </h1>
""", unsafe_allow_html=True)

msg=st.text_input("Enter text", placeholder="e.g: Hello, How are you?")
if st.button("Prediction",key="b2"):
    pred=language_model.predict([msg])
    st.success(pred[0])

st.markdown("#### OR")
uploaded_file = st.file_uploader("Choose a file",type=["csv", "txt"],key="u3")

        
if uploaded_file:
        
    df=pd.read_csv(uploaded_file,header=None,names=['Msg'])

    pred=language_model.predict(df.Msg)
    df.index=range(1,df.shape[0]+1)
    df["Prediction"]=pred
    st.dataframe(df)