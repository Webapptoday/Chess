import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from PIL import Image
import re

# Setup credentials
creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = gspread.authorize(creds)
sheet = client.open("ChessLegends_Users").sheet1

# Store session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Images for coaches
dhairya_img = Image.open("dhairya.png")
shouri_img = Image.open("shouri.png")

# Helper to validate inputs
def is_valid_name(name):
    return len(name.strip()) > 3

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) and len(email.split("@")[0]) > 3

def save_user(name, email):
    existing = sheet.get_all_records()
    for row in existing:
        if row["Email"] == email:
            return True
    sheet.append_row([name, email])
    return True

def login_screen():
    st.title("♟️ Chess Legends")
    st.subheader("Sharpen Your Game. Become a Legend.")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    if st.button("Sign Up / Login"):
        if not is_valid_name(name):
            st.error("Full Name must be more than 3 characters.")
            return
        if not is_valid_email(email):
            st.error("Email must be valid and more than 3 characters before '@'.")
            return
        save_user(name, email)
        st.session_state.logged_in = True
        st.session_state.user_name = name

    st.markdown("Already signed up?")
    if st.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""

def coach_card(name, img, bio, price, coach_key):
    st.image(img, width=250)
    st.markdown(f"### {name}")
    st.markdown(bio)
    st.markdown(f"**Price:** {price}")
    if st.button(f"View {name}'s Profile", key=coach_key):
        st.session_state["selected_coach"] = coach_key
    st.markdown("---")

def coach_profile(name, img, bio, price):
    st.image(img, width=300)
    st.markdown(f"## {name}")
    st.markdown(bio)
    st.markdown(f"**Price:** {price}")
    st.markdown("### [📋 Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/edit)", unsafe_allow_html=True)
    if st.button("Back to Coaches"):
        st.session_state["selected_coach"] = None

def main_app():
    st.sidebar.title(f"Welcome, {st.session_state.user_name}")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        return

    selected = st.session_state.get("selected_coach")

    if selected == "dhairya":
        coach_profile(
            name="Dhairya",
            img=dhairya_img,
            bio="State Chess Champion 2025. Strategic, fun-focused lessons.",
            price="$20/session",
        )
    elif selected == "shouri":
        coach_profile(
            name="Shouri",
            img=shouri_img,
            bio="Tactical wizard with top 1% national ranking. Inspires passion.",
            price="$25/session",
        )
    else:
        st.title("🧠 Choose Your Chess Coach")
        st.write("Learn from the best. Tap a card to see details and sign up.")
        col1, col2 = st.columns(2)
        with col1:
            coach_card(
                name="Dhairya",
                img=dhairya_img,
                bio="State Champion | Kids Welcome | Fun + Strategy",
                price="$20/session",
                coach_key="dhairya"
            )
        with col2:
            coach_card(
                name="Shouri",
                img=shouri_img,
                bio="Top 1% Tactics | Deep Theory | Rapid Growth",
                price="$25/session",
                coach_key="shouri"
            )

# App entry point
if st.session_state.logged_in:
    main_app()
else:
    login_screen()
