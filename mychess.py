import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Load credentials from secrets
creds_dict = st.secrets["gcp_service_account"]
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

# Authorize the client
client = gspread.authorize(creds)

# Open the spreadsheet by key
sheet = client.open_by_key("10-YFBO0ILhR3T8aL8j6oBctaCZifKqxcSuNdzmfTNG0").sheet1

# Read and display values
data = sheet.get_all_records()
st.write(data)
