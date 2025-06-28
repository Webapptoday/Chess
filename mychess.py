import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Load credentials from Streamlit secrets
creds_dict = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

# Connect to the Google Sheet
client = gspread.authorize(creds)
sheet = client.open("ChessLegends_Users").sheet1

# Function to append a new row
def append_row(data):
    sheet.append_row(data)
