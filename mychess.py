import streamlit as st

# Apply custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
