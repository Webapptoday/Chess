import streamlit as st

# -------------------- CSS --------------------
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

    .coach-card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
    }

    .coach-name {
        font-weight: bold;
        font-size: 1.3rem;
        color: #1f4e96;
    }

    .coach-link {
        color: #1f4e96;
        text-decoration: underline;
        cursor: pointer;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- Session State --------------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if "success_msg" not in st.session_state:
    st.session_state.success_msg = ""

if "page" not in st.session_state:
    st.session_state.page = "login"

# -------------------- Pages --------------------

def login_signup_screen():
    st.session_state.page = "login"
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
            st.session_state.page = "coach_select"
            st.rerun()
        else:
            st.warning("Please enter both your name and email.")

    if st.button("Log In"):
        if email in st.session_state.users:
            st.session_state.logged_in_user = email
            st.session_state.success_msg = f"Welcome back, {st.session_state.users[email]}!"
            st.session_state.page = "coach_select"
            st.rerun()
        else:
            st.error("No account found. Please sign up first.")
    st.markdown('</div>', unsafe_allow_html=True)

def coach_selection_screen():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">Select Your Coach</div>', unsafe_allow_html=True)

    st.markdown('<div class="coach-card">', unsafe_allow_html=True)
    st.markdown('<div class="coach-name">Coach Dhairya</div>', unsafe_allow_html=True)
    if st.button("See Coach Dhairya's Profile"):
        st.session_state.page = "dhairya"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="coach-card">', unsafe_allow_html=True)
    st.markdown('<div class="coach-name">Coach Shouri</div>', unsafe_allow_html=True)
    if st.button("See Coach Shouri's Profile"):
        st.session_state.page = "shouri"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Log Out"):
        st.session_state.logged_in_user = None
        st.session_state.page = "login"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def coach_dhairya_profile():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">Coach Dhairya</div>', unsafe_allow_html=True)
    st.markdown("♟️ National Chess Champion, Expert in Opening Theory and Tactics. Loves working with beginners and intermediates.")
    st.image("https://via.placeholder.com/400x250?text=Coach+Dhairya", use_column_width=True)
    if st.button("Back to Coach Selection"):
        st.session_state.page = "coach_select"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def coach_shouri_profile():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">Coach Shouri</div>', unsafe_allow_html=True)
    st.markdown("♟️ Puzzle Master & Endgame Specialist. Known for helping students boost their rating with precision practice.")
    st.image("https://via.placeholder.com/400x250?text=Coach+Shouri", use_column_width=True)
    if st.button("Back to Coach Selection"):
        st.session_state.page = "coach_select"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- Routing Logic --------------------
if not st.session_state.logged_in_user:
    login_signup_screen()
elif st.session_state.page == "coach_select":
    coach_selection_screen()
elif st.session_state.page == "dhairya":
    coach_dhairya_profile()
elif st.session_state.page == "shouri":
    coach_shouri_profile()
else:
    coach_selection_screen()
