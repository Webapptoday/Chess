import streamlit as st

# Apply custom CSS
# Inline CSS injection
st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }

    .header {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        padding: 1rem;
        color: #0066cc;
        border-bottom: 2px solid #e0e0e0;
        margin-bottom: 1rem;
    }

    .form-container {
        padding: 2rem;
        background-color: #f9f9f9;
        border-radius: 12px;
        max-width: 500px;
        margin: 0 auto;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }

    button {
        background-color: #0077cc !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)
# In-memory user simulation
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if "success_msg" not in st.session_state:
    st.session_state.success_msg = ""

def login_screen():
    st.markdown('<div class="header">🚗 DriveHero</div>', unsafe_allow_html=True)
    st.subheader("Safe Driving Starts Here")

    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    full_name = st.text_input("Full Name", key="name_input")
    email = st.text_input("Email Address", key="email_input")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up for an Account"):
            if email and full_name:
                st.session_state.users[email] = full_name
                st.session_state.logged_in_user = email
                st.session_state.success_msg = "Account created successfully"
            else:
                st.warning("Please enter both name and email.")
    with col2:
        if st.button("Log In"):
            if email in st.session_state.users:
                st.session_state.logged_in_user = email
                st.session_state.success_msg = f"Welcome back, {st.session_state.users[email]}"
            else:
                st.error("Account not found. Please sign up first.")
    st.markdown('</div>', unsafe_allow_html=True)

def welcome_screen():
    st.markdown('<div class="header">✅ DriveHero</div>', unsafe_allow_html=True)
    st.success(st.session_state.success_msg)
    if st.button("Log Out"):
        del st.session_state.users[st.session_state.logged_in_user]
        st.session_state.logged_in_user = None
        st.session_state.success_msg = ""

if st.session_state.logged_in_user:
    welcome_screen()
else:
    login_screen()
