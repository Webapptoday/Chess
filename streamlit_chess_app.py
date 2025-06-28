import streamlit as st
import re
import gspread
from google.oauth2.service_account import Credentials

# Set page config
st.set_page_config(page_title="Chess Legends", layout="centered")

# Blue background CSS
st.markdown(
    """
    <style>
        body {
            background-color: #e6f0ff;
        }
        .stApp {
            background-color: #e6f0ff;
        }
        .title {
            color: #003366;
        }
        .error-text {
            color: red;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Google Sheets setup
SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPE,
)
client = gspread.authorize(creds)
sheet = client.open("ChessLegends_Users").sheet1

# Navigation
page = st.sidebar.radio("Navigation", ["Home", "Coaches", "Register"])

if page == "Home":
    st.title("♟️ Welcome to Chess Legends")
    st.write("Join us to elevate your chess game with the best coaches and exciting lessons!")
    st.markdown("[Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/viewform)", unsafe_allow_html=True)

elif page == "Coaches":
    st.title("Meet Our Coaches")

    st.subheader("♟️ Dhairya Mehta")
    st.image("Dhairya Mehta.png", width=300, caption="Dhairya Mehta")
    st.write("State champion, expert in positional strategy.")

    st.subheader("♟️ Shouri")
    st.image("Shouri.png", width=300, caption="Shouri")
    st.write("Tactical wizard and dynamic trainer.")

elif page == "Register":
    st.title("📋 Register")

    name = st.text_input("Enter your name")
    email_input = st.text_input("Enter your email")

    # Validate inputs
    name_valid = len(name.strip()) > 3
    email_valid = re.match(r"^[^@]{4,}@example\.com$", email_input.strip())

    if st.button("Submit"):
        if not name_valid or not email_valid:
            if not name_valid:
                st.error("Name must be more than 3 characters.")
            if not email_valid:
                st.error("Email must be valid and follow the format: yourname@example.com (with at least 4 characters before '@').")
        else:
            sheet.append_row([name, email_input])
            st.success("✅ Registration successful!")

    # Google Form
    st.markdown("---")
    st.markdown("Or register using our Google Form:")
    st.markdown(
        "[📝 Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/viewform)",
        unsafe_allow_html=True,
    )
