import streamlit as st
from PIL import Image
import gspread
from google.oauth2.service_account import Credentials
import streamlit as st
import json

# Load credentials from Streamlit secrets
creds_dict = st.secrets["gcp_service_account"]
credentials = Credentials.from_service_account_info(dict(creds_dict))

client = gspread.authorize(credentials)
sheet = client.open("ChessLegends_Users").sheet1

client = gspread.authorize(creds)
sheet = client.open("ChessLegends_Users").sheet1

# Page navigation
page = st.sidebar.selectbox("Go to", ["Home", "Dhairya", "Shouri"])

def show_coach_profile(name, image_file, description, price):
    st.title(name)
    st.image(image_file, use_column_width=True)
    st.subheader("About")
    st.write(description)
    st.subheader("Price")
    st.write(price)
    st.markdown(
        '[📋 Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg)',
        unsafe_allow_html=True,
    )

if page == "Home":
    st.title("Welcome to Chess Legends")

    st.subheader("Create Account")

    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email (example@example.com)")

    # Simple validation
    if st.button("Sign Up"):
        if len(name) < 3:
            st.error("Name must be at least 3 characters.")
        elif len(email.split("@")[0]) < 3 or not email.endswith("@example.com"):
            st.error("Email must be in the format ***@example.com with at least 3 characters before @.")
        else:
            sheet.append_row([name, email])
            st.success("Account created successfully!")

    st.subheader("Choose Your Coach")

    col1, col2 = st.columns(2)
    with col1:
        st.image("fcb23e8f-e35d-49fe-9b5d-855cbfe24d1f.png", caption="Dhairya")
        if st.button("Meet Dhairya"):
            st.session_state.page = "Dhairya"
            st.experimental_rerun()
    with col2:
        st.image("5ad12b44-462e-42a6-87f2-85545ab5c56b.png", caption="Shouri")
        if st.button("Meet Shouri"):
            st.session_state.page = "Shouri"
            st.experimental_rerun()

elif page == "Dhairya":
    show_coach_profile(
        "Coach Dhairya",
        "fcb23e8f-e35d-49fe-9b5d-855cbfe24d1f.png",
        "Dhairya is an experienced chess player and coach.",
        "$20/hr",
    )

elif page == "Shouri":
    show_coach_profile(
        "Coach Shouri",
        "5ad12b44-462e-42a6-87f2-85545ab5c56b.png",
        "Shouri is a fun and strategic chess instructor.",
        "$18/hr",
    )
