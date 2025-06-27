import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from gspread.exceptions import SpreadsheetNotFound
import re

# Set Streamlit page config
st.set_page_config(page_title="ChessLegends", layout="centered")

# Load Google Sheets credentials from secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scope)
client = gspread.authorize(creds)

# Google Sheet name
SHEET_NAME = "ChessLegends_Users"

# Create or get the worksheet
@st.cache_resource
def get_worksheet():
    try:
        sheet = client.open(SHEET_NAME)
    except SpreadsheetNotFound:
        # Auto-create if it doesn't exist
        sheet = client.create(SHEET_NAME)
        sheet.share(st.secrets["gcp_service_account"]["client_email"], perm_type="user", role="writer")
    return sheet.sheet1

worksheet = get_worksheet()

# Page UI
st.markdown("## ♟️ ChessLegends")
st.markdown("### Sharpen Your Skills One Move at a Time")
st.markdown("---")

fullname = st.text_input("Full Name")
email = st.text_input("Email Address")

col1, col2 = st.columns(2)

with col1:
    if st.button("Sign Up for an Account"):
        # Validation
        if len(fullname.strip()) < 3:
            st.error("Full name must be at least 3 characters long.")
            st.stop()

        match = re.match(r"^([^@]{3,})@[^@]+\.[^@]+$", email)
        if not match:
            st.error("Enter a valid email address (minimum 3 characters before '@').")
            st.stop()

        # Check if already signed up
        records = worksheet.get_all_records()
        if any(r["Email"] == email for r in records):
            st.warning("This email is already registered. Please log in.")
        else:
            worksheet.append_row([fullname, email])
            st.success("🎉 Account created successfully!")

with col2:
    if st.button("Log In"):
        records = worksheet.get_all_records()
        user = next((r for r in records if r["Email"] == email), None)
        if user:
            st.success(f"Welcome back, {user['Full Name']}!")
        else:
            st.error("No account found with this email.")
