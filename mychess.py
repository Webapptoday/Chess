import streamlit as st

# --- Apply inline CSS to match ChessLegends design ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', sans-serif;
    }

    .app-card {
        max-width: 450px;
        margin: 50px auto;
        padding: 2rem;
        background: white;
        border-radius: 18px;
        box-shadow: 0 6px 24px rgba(0,0,0,0.1);
        text-align: center;
    }

    .app-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f4e96;
        margin-bottom: 0.25rem;
    }

    .app-subtitle {
        font-size: 1rem;
        color: #426ea8;
        margin-bottom: 2rem;
    }

    .stButton button {
        width: 100%;
        padding: 0.75rem;
        border-radius: 10px !important;
        font-weight: bold;
        background-color: #1f4e96 !important;
        color: white !important;
        margin-top: 0.75rem;
    }

    .success-msg {
        font-size: 1.2rem;
        color: #2d8a34;
        margin: 1rem 0;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- User session and account simulation ---
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if "success_msg" not in st.session_state:
    st.session_state.success_msg = ""

# --- Login/Signup Page ---
def login_signup_screen():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">ChessLegends</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Sharpen Your Skills One Move at a Time</div>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    if st.button("Sign Up for an Account"):
        if name and email:
            st.session_state.users[email] = name
            st.session_state.logged_in_user = email
            st.session_state.success_msg = f"Welcome, {name}!"
            st.rerun()
        else:
            st.warning("Please enter both your name and email.")

    if st.button("Log In"):
        if email in st.session_state.users:
            st.session_state.logged_in_user = email
            st.session_state.success_msg = f"Welcome back, {st.session_state.users[email]}!"
            st.rerun()
        else:
            st.error("No account found. Please sign up first.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Post-login success screen ---
def success_screen():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">Welcome!</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="success-msg">{st.session_state.success_msg}</div>', unsafe_allow_html=True)

    if st.button("Log Out"):
        st.session_state.logged_in_user = None
        st.session_state.success_msg = ""
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- Route Logic ---
if st.session_state.logged_in_user:
    success_screen()
else:
    login_signup_screen()
