import streamlit as st

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }

    .app-card {
        max-width: 450px;
        margin: 50px auto;
        padding: 2rem;
        background: white;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        text-align: center;
    }

    .app-header {
        font-size: 2.2rem;
        font-weight: 600;
        color: #274060;
        margin-bottom: 0.5rem;
    }

    .app-subtitle {
        font-size: 1.1rem;
        color: #5c7c9c;
        margin-bottom: 1.5rem;
    }

    .stButton button {
        width: 100%;
        padding: 0.75rem;
        border-radius: 8px;
        font-weight: bold;
        margin-top: 1rem;
    }

    .success-box {
        font-size: 1.2rem;
        color: green;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# In-memory store
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if "success_msg" not in st.session_state:
    st.session_state.success_msg = ""

def login_signup_screen():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">DriveHero</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Safe Driving Starts Here</div>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    sign_up = st.button("Sign Up for an Account")
    log_in = st.button("Log In")

    if sign_up:
        if name and email:
            st.session_state.users[email] = name
            st.session_state.logged_in_user = email
            st.session_state.success_msg = "Account created successfully."
            st.rerun()
        else:
            st.warning("Please enter both name and email.")

    if log_in:
        if email in st.session_state.users:
            st.session_state.logged_in_user = email
            st.session_state.success_msg = f"Welcome back, {st.session_state.users[email]}!"
            st.rerun()
        else:
            st.error("No account found. Please sign up first.")
    st.markdown('</div>', unsafe_allow_html=True)

def success_screen():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">✅ Success</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="success-box">{st.session_state.success_msg}</div>', unsafe_allow_html=True)

    if st.button("Log Out"):
        st.session_state.logged_in_user = None
        st.session_state.success_msg = ""
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Route to appropriate screen
if st.session_state.logged_in_user:
    success_screen()
else:
    login_signup_screen()
