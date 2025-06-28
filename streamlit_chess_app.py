import streamlit as st
from PIL import Image
import webbrowser

# --- Page Config ---
st.set_page_config(page_title="Chess Legends", layout="centered")

# --- Custom CSS for blue background ---
st.markdown(
    """
    <style>
        body {
            background-color: #e6f0ff;
        }
        .main {
            background-color: #e6f0ff;
        }
        .stApp {
            background-color: #e6f0ff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Navigation ---
page = st.sidebar.selectbox("Choose a page", ["Home", "Our Coaches", "Register"])

# --- Home Page ---
if page == "Home":
    st.title("♟️ Welcome to Chess Legends!")
    st.markdown("Where strategy meets passion. Sharpen your skills with our experienced coaches.")

# --- Coaches Page ---
elif page == "Our Coaches":
    st.header("Meet Our Coaches")

    col1, col2 = st.columns(2)

    with col1:
        try:
            dhairya_img = Image.open("dhairya.png")
            st.image(dhairya_img, caption="Coach Dhairya", use_column_width=True)
        except:
            st.warning("Coach Dhairya image not found.")

    with col2:
        try:
            shouri_img = Image.open("shouri.png")
            st.image(shouri_img, caption="Coach Shouri", use_column_width=True)
        except:
            st.warning("Coach Shouri image not found.")

# --- Registration Page ---
elif page == "Register":
    st.header("Register for Lessons")
    st.markdown("Fill out the form below to get started with your chess journey.")
    st.markdown("[📋 Register Now](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg/edit)", unsafe_allow_html=True)
