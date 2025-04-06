import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Abhishek", layout="wide")

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Disease Detection", "Crop Recommendation", "Fertilizer Suggestion", "Action Advisory", "About"],
        icons=["house", "activity", "bar-chart", "flask", "lightbulb", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Main Header
st.markdown("<h1 style='text-align: center; color: green;'>Abhishek</h1>", unsafe_allow_html=True)
st.markdown("---")

# Home
if selected == "Home":
    st.subheader("Welcome to Chut-Paglu 🌾")
    st.write("""
        Chut-Paglu is your one-stop smart farming assistant. 
        This platform helps farmers and agricultural enthusiasts make better decisions using technology-driven solutions:

        - 🌱 Plant Disease Detection
        - 🌾 Crop Recommendation System
        - 💊 Fertilizer Suggestion
        - 📈 Actionable Advisory based on weather and agricultural trends
    """)

    st.markdown("## 🚀 Explore Services")

    col1, col2 = st.columns(2)

    with col1:
        st.page_link("pages/disease_detection.py", label="🔍 Disease Detection", icon="🦠")

    with col2:
        st.page_link("pages/crop_recommendation.py", label="🌿 Crop Recommendation", icon="🌾")

    with col1:
        st.page_link("pages/fertilizer_suggestion.py", label="💊 Fertilizer Suggestion", icon="🧪")

    with col2:
        st.page_link("pages/action_advisory.py", label="📈 Action Advisory", icon="📊")

# About Page
elif selected == "About":
    st.subheader("About Chut-Paglu")
    st.write("This application was built by Abhishek and their teammate to support farmers with machine learning–driven tools and solutions.")
