
import streamlit as st
import joblib
import pandas as pd

spam_model=joblib.load("spam_classifier.pkl")
language_model=joblib.load("lang_det.pkl")
news_model=joblib.load("news_catH.pkl")
review_model=joblib.load("review.pkl")


# Page config
# Page config
st.set_page_config(page_title="Multi-Model NLP App", page_icon="🤖", layout="centered")

# st.markdown(
#     """
#     <style>
#     /* 🌈 Gradient background for the whole app */
#     .stApp {
#         background: linear-gradient(135deg, #d3f5f8, #e1bee7);
#         background-attachment: fixed;
#         background-size: cover;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

import base64

def set_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image path
set_bg_from_local("bg1.jpg")  # Replace with your actual file name



#dropdown color
st.markdown("""
    <style>
    /* Change background of the selectbox */
    div[data-baseweb="select"] {
        background-color: black !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Style the dropdown options */
    div[data-baseweb="select"] * {
        background-color: black !important;
        color: white !important;
    }

    /* Optional: Style label above the dropdown */
    label {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

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



# ----------------- SIDEBAR ------------------
st.sidebar.title("🔍 More to do")
page = st.sidebar.radio("Go to:", ["🏠 Home","📂 About Project", "🙋‍♀️ About Me", "📞 Contact Info"])

st.sidebar.markdown("---")


if page == "🏠 Home":
    st.markdown("""
    <h1 style="font-family:sans-serif;">
        <span style="color:#f3e449;">LENS</span> <span style="color:#ffffff;">e</span><span style="color:#f3e449;">X</span><span style="color:#ffffff;">pert</span>
    </h1>
        """, unsafe_allow_html=True)
                


    st.markdown("""
        <h1 style="font-family:sans-serif;">
            <span style="color:#ffffff;">Welcome to a (NLP Suite)! 👋</span>
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        .custom-h3 {
            font-family: sans-serif;
            font-size: 1.5em;  /* Optional: tweak size */
            color: #ffffff;
        }
        </style>

        <h3 class="custom-h3">What would you like to do?</h3>
    """, unsafe_allow_html=True)


    model_option = st.selectbox(
        "Choose a model:",
        (
            "🔽 Select a model",
            "📊 Restaurant Sentiment Analysis",
            "📰 News Classifier",
            "✉️ Spam Classifier",
            "🌐 Language Detection"
        )
    )

    if model_option != "🔽 Select a model":
        if st.button("Continue"):
            if model_option == "🍽️ Restaurant Sentiment Analysis":
                st.switch_page("LensX/pages/Review_model.py")
            elif model_option == "📰 News Classifier":
                st.switch_page("LensX/pages/News_model.py")
            elif model_option == "✉️ Spam Classifier":
                st.switch_page("LensX/pages/Spam_model.py")
            elif model_option == "🌐 Language Detection":
                st.switch_page("Lens/pages/Language_model.py")





# ----------------- ABOUT ME SECTION ------------------
elif page == "🙋‍♀️ About Me":

    about_me = """
    # <span style="color:yellow;">About Me</span>
    **<span style="color:white;">Hi, I'm Bhumika Sharma!</span>**  
    <span style="color:white;">A passionate data analyst and aspiring data scientist.</span>  
    <span style="color:white;">I love working on real-world NLP problems and building intelligent systems that help users make better decisions.</span>  

    **<span style="color:white;">Skills</span>**<span style="color:white;">: Python, SQL, Streamlit, Power BI, Machine Learning, NLP</span>  
    **<span style="color:white;">Projects</span>**<span style="color:white;">: Sentiment Analysis, News Classification, Spam Detection, Language Identification </span> 
    """
    st.markdown(about_me, unsafe_allow_html=True)




# ----------------- CONTACT SECTION ------------------
elif page == "📞 Contact Info":
    contact_info = """
    <h1 style="color:yellow;">Contact Information</h1>

    <p style="color:white;">📧 <strong>Email:</strong> bhumikasharma1808@gmail.com</p>
    <p style="color:white;">💼 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/098bhumika" style="color:white;" target="_blank">www.linkedin.com/in/098bhumika</a></p>
    <p style="color:white;">🐱 <strong>GitHub:</strong> <a href="https://github.com/Bhumika1808" style="color:white;" target="_blank">github.com/Bhumika1808</a></p>

    <h3 style="color:white;">Any Suggestions for this Project?</h3>
    """

    st.markdown(contact_info, unsafe_allow_html=True)

#----------------- about project------------------

elif page == "📂 About Project":
    about_project = """
    <h1 style="color:yellow;">About the Project</h1>

    <p style="color:white;">
    <b>LENS eXpert (NLP Suits)</b> is a multi-functional Natural Language Processing platform that hosts four powerful models:
    </p>

    <ol style="color:white;">
        <li>📊 <b>Restaurant Review Sentiment Analysis</b> – Understand customer sentiment from their reviews.</li>
        <li>✉️ <b>Spam Classifier</b> – Identify spam messages with high accuracy.</li>
        <li>🌐 <b>Language Detection</b> – Automatically detect the language of a given text.</li>
        <li>📰 <b>News Classifier</b> – Categorize news articles into relevant categories.</li>
    </ol>

    <p style="color:white;">
    The goal of this app is to demonstrate the real-world utility of NLP models built using Python, Scikit-learn, and Streamlit.
    </p>

    <hr style="border-top: 1px solid white;">
    """

    st.markdown(about_project, unsafe_allow_html=True)

    
