import streamlit as st
import sqlite3
import re
from datetime import datetime

# -------------------------------
# Database Setup
# -------------------------------
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL
)''')
conn.commit()

# -------------------------------
# Email Validation
# -------------------------------
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
def is_valid_email_syntax(email):
    return re.match(email_regex, email) is not None

# -------------------------------
# Session State Management
# -------------------------------
if "user" not in st.session_state:
    st.session_state.user = None
    st.session_state.message = ""

# -------------------------------
# Styling
# -------------------------------
st.markdown("""
    <style>
        body {
            background-color: #e0f0ff;
        }
        .coach-card {
            border: 2px solid #007bff;
            padding: 1em;
            border-radius: 10px;
            margin-bottom: 1em;
            background-color: white;
        }
        .coach-header {
            font-size: 1.5em;
            color: #007bff;
            margin-bottom: 0.5em;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Login/Signup Interface
# -------------------------------
def login_signup():
    st.title("ChessLegends")
    st.subheader("Champions are made here")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up"):
            if len(name.strip()) < 3:
                st.error("Name must be at least 3 characters long.")
            elif not is_valid_email_syntax(email):
                st.error("Invalid email address.")
            else:
                try:
                    c.execute("INSERT INTO users (name, email, created_at) VALUES (?, ?, ?)",
                              (name.strip(), email.strip(), datetime.utcnow().isoformat()))
                    conn.commit()
                    st.session_state.user = name
                    st.session_state.message = "Account created successfully!"
                except sqlite3.IntegrityError:
                    st.error("An account with this email already exists.")
    with col2:
        if st.button("Log In"):
            c.execute("SELECT name FROM users WHERE email = ?", (email.strip(),))
            user = c.fetchone()
            if user:
                st.session_state.user = user[0]
                st.session_state.message = f"Welcome back, {user[0]}!"
            else:
                st.error("No account found with that email.")

# -------------------------------
# Welcome Screen & Coaches
# -------------------------------
def show_dashboard():
    st.title("Welcome " + st.session_state.user)
    st.success(st.session_state.message)

    st.markdown("<h2 style='color:#007bff;'>View our Coaches</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='coach-card'>
            <div class='coach-header'>Dhairya M</div>
            <p>USCF 2150 • 150+ tournaments • Summer camp coach</p>
            <p><strong>$25/hr (Online)</strong>, <strong>$40/hr (In-person)</strong></p>
            <p><strong>$30/hr group</strong></p>
            <a href='https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg' target='_blank'>Book your class HERE</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='coach-card'>
            <div class='coach-header'>Shouri M</div>
            <p>USCF 1700 • 180+ tournaments • Experienced youth coach</p>
            <p><strong>$30/hr (Online)</strong>, <strong>$45/hr (In-person)</strong></p>
            <p><strong>$30/hr group</strong></p>
            <a href='https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg' target='_blank'>Book your class HERE</a>
        </div>
        """, unsafe_allow_html=True)

    st.button("Log Out", on_click=lambda: st.session_state.update(user=None, message=""))

# -------------------------------
# App Logic
# -------------------------------
if st.session_state.user:
    show_dashboard()
else:
    login_signup()
