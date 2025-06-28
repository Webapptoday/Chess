import gspread
import streamlit as st
from google.oauth2.service_account import Credentials

# Load credentials from secrets
creds_dict = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

# Connect to Google Sheets
client = gspread.authorize(creds)
sheet = client.open("ChessLegends_Users").sheet1
