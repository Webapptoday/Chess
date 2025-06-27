import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# -------------------- Google Sheets Setup --------------------
@st.cache_resource
def get_worksheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_dict = dict(st.secrets["google_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open("chesslegends_users").sheet1
    return sheet

sheet = get_worksheet()

# -------------------- Helpers --------------------
@st.cache_data(ttl=60)
def load_users():
    records = sheet.get_all_records()
    return {record['Email']: record['Full Name'] for record in records}

def add_user(name, email):
    sheet.append_row([name, email])

# -------------------- Session State --------------------
if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None
if "page" not in st.session_state:
    st.session_state.page = "login"

# -------------------- Screens --------------------
def login_screen():
    st.title("♟ ChessLegends")
    st.subheader("Sharpen Your Skills One Move at a Time")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    users = load_users()

    if st.button("Sign Up"):
        if name and email:
            if email not in users:
                add_user(name, email)
                st.success("Account created!")
                st.session_state.logged_in_user = email
                st.session_state.page = "dashboard"
                st.rerun()
            else:
                st.warning("Account already exists. Please log in.")
        else:
            st.warning("Please enter both fields.")

    if st.button("Log In"):
        if email in users:
            st.session_state.logged_in_user = email
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("Account not found.")

def dashboard():
    users = load_users()
    name = users.get(st.session_state.logged_in_user, "Coach")
    st.title(f"Welcome, {name}!")
    st.write("Select a coach to view pricing:")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Coach Dhairya")
        st.write("National Champion • Opening Theory")
        if st.button("Dhairya's Pricing"):
            st.session_state.page = "pricing_dhairya"

    with col2:
        st.subheader("Coach Shouri")
        st.write("Endgame Expert • Puzzle Master")
        if st.button("Shouri's Pricing"):
            st.session_state.page = "pricing_shouri"

    st.markdown("---")
    if st.button("Log Out"):
        st.session_state.logged_in_user = None
        st.session_state.page = "login"
        st.rerun()

def pricing(coach_name):
    st.title(f"{coach_name} - Pricing")
    st.markdown("💵 **$25/hour** coaching")
    st.markdown("✅ Personalized training\n✅ Weekly assignments\n✅ Tactics and game review")
    if st.button("⬅ Back to Coaches"):
        st.session_state.page = "dashboard"

# -------------------- Router --------------------
if not st.session_state.logged_in_user:
    login_screen()
elif st.session_state.page == "dashboard":
    dashboard()
elif st.session_state.page == "pricing_dhairya":
    pricing("Coach Dhairya")
elif st.session_state.page == "pricing_shouri":
    pricing("Coach Shouri")
