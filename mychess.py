import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json
import re

# Set up page layout
st.set_page_config(page_title="Chess Legends", layout="centered")

st.markdown("""
    <style>
        body { background-color: #e6f0ff; }
        .stApp { background-color: #e6f0ff; }
        .title { color: #003366; font-size: 2.5em; font-weight: bold; }
        .error-text { color: red; }
    </style>
""", unsafe_allow_html=True)

# Setup Google Sheets credentials from Streamlit Secrets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds_dict = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open("ChessLegends_Users").sheet1

# Navigation
page = st.sidebar.radio("Navigate", ["Home", "Coaches", "Register"])

if page == "Home":
    st.markdown('<h1 class="title">♟️ Welcome to Chess Legends</h1>', unsafe_allow_html=True)
    st.write("Join our interactive chess camp and train with champions.")
    st.markdown("[📝 Register Now (Google Form)](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/viewform)", unsafe_allow_html=True)

elif page == "Coaches":
    st.markdown('<h1 class="title">Meet Our Coaches</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Dhairya Mehta")
        st.image("Dhairya Mehta.png", caption="State Champion", use_column_width=True)
        st.markdown("[💵 $25/hr - Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/viewform)", unsafe_allow_html=True)

    with col2:
        st.subheader("Shouri")
        st.image("Shouri.png", caption="Tactical Finalist", use_column_width=True)
        st.markdown("[💵 $25/hr - Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/viewform)", unsafe_allow_html=True)

elif page == "Register":
    st.markdown('<h1 class="title">📋 Register Here</h1>', unsafe_allow_html=True)
    name = st.text_input("Enter your full name")
    email = st.text_input("Enter your email (must be at least 4 characters before @example.com)")

    name_valid = len(name.strip()) > 3
    email_valid = re.match(r"^[^@]{4,}@example\.com$", email.strip())

    if st.button("Submit"):
        if not name_valid:
            st.error("❌ Name must be more than 3 characters.")
        if not email_valid:
            st.error("❌ Email must have at least 4 characters before '@example.com'.")
        if name_valid and email_valid:
            sheet.append_row([name, email])
            st.success("✅ Registration successful!")

    st.markdown("---")
    st.markdown("[📝 Or register using Google Form](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/viewform)", unsafe_allow_html=True)
