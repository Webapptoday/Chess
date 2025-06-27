import streamlit as st

# -------------------- CSS --------------------
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;
        font-family: 'Segoe UI', sans-serif;
    }

    .app-card {
        max-width: 600px;
        margin: 40px auto;
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
        margin-bottom: 0.5rem;
    }

    .success-msg {
        font-size: 1.2rem;
        color: #2d8a34;
        margin: 1rem 0;
        font-weight: bold;
    }

    .coach-grid {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        gap: 2rem;
        margin-top: 2rem;
        flex-wrap: wrap;
    }

    .coach-card {
        background: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        padding: 1.5rem;
        width: 250px;
        text-align: center;
    }

    .coach-name {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1f4e96;
        margin-bottom: 0.5rem;
    }

    .coach-description {
        font-size: 0.95rem;
        margin-bottom: 1rem;
        color: #333;
    }

    .stButton button {
        width: 100%;
        padding: 0.7rem;
        border-radius: 10px !important;
        font-weight: bold;
        background-color: #1f4e96 !important;
        color: white !important;
        margin-top: 0.75rem;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- Session State --------------------
if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

if "page" not in st.session_state:
    st.session_state.page = "login"

if "success_msg" not in st.session_state:
    st.session_state.success_msg = ""

# -------------------- Screens --------------------

def login_signup_screen():
    st.session_state.page = "login"
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown('<div class="app-header">ChessLegends</div>', unsafe_allow_html=True)
    st.subheader("Sharpen Your Skills One Move at a Time")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    if st.button("Sign Up for an Account"):
        if name and email:
            st.session_state.users[email] = name
            st.session_state.logged_in_user = email
            st.session_state.success_msg = f"Welcome, {name}!"
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.warning("Please enter both your name and email.")

    if st.button("Log In"):
        if email in st.session_state.users:
            st.session_state.logged_in_user = email
            st.session_state.success_msg = f"Welcome back, {st.session_state.users[email]}!"
            st.session_state.page = "dashboard"
            st.rerun()
        else:
            st.error("No account found. Please sign up first.")
    st.markdown('</div>', unsafe_allow_html=True)

def coach_pricing_page(coach_name):
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="app-header">{coach_name} Pricing</div>', unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:1.2rem;'>💰 Coaching Rate: <strong>$25/hour</strong></p>", unsafe_allow_html=True)
    if st.button("⬅ Back to Coaches"):
        st.session_state.page = "dashboard"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

def dashboard_screen():
    name = st.session_state.users[st.session_state.logged_in_user]
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="app-header">Welcome!</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="success-msg">Welcome, {name}!</div>', unsafe_allow_html=True)

    st.markdown('<div class="coach-grid">', unsafe_allow_html=True)

    # Coach Dhairya
    with st.container():
        st.markdown('<div class="coach-card">', unsafe_allow_html=True)
        st.markdown('<div class="coach-name">Coach Dhairya</div>', unsafe_allow_html=True)
        st.markdown('<div class="coach-description">National Chess Champion. Expert in openings and tactical play.</div>', unsafe_allow_html=True)
        if st.button("View Dhairya's Pricing"):
            st.session_state.page = "pricing_dhairya"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Coach Shouri
    with st.container():
        st.markdown('<div class="coach-card">', unsafe_allow_html=True)
        st.markdown('<div class="coach-name">Coach Shouri</div>', unsafe_allow_html=True)
        st.markdown('<div class="coach-description">Endgame strategist. Helps students master positional understanding.</div>', unsafe_allow_html=True)
        if st.button("View Shouri's Pricing"):
            st.session_state.page = "pricing_shouri"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Log Out"):
        st.session_state.logged_in_user = None
        st.session_state.page = "login"
        st.rerun()

# -------------------- Router --------------------
if not st.session_state.logged_in_user:
    login_signup_screen()
elif st.session_state.page == "dashboard":
    dashboard_screen()
elif st.session_state.page == "pricing_dhairya":
    coach_pricing_page("Coach Dhairya")
elif st.session_state.page == "pricing_shouri":
    coach_pricing_page("Coach Shouri")
else:
    dashboard_screen()
