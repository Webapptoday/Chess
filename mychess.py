import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Chess Legends",
    page_icon="♟️",
    layout="wide",
)

# Sidebar navigation
st.markdown(
    """
    <style>
        .css-1544g2n {padding-top: 1rem;}
        .css-1d391kg, .css-1avcm0n {font-size: 1.2rem !important;}
        .sidebar .sidebar-content {
            padding-top: 2rem;
        }
        .block-container {
            padding-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load logo
logo_url = "https://i.postimg.cc/vBZcwTSH/Chat-GPT-Image-Jul-2-2025-10-04-14-AM.png"
response = requests.get(logo_url)
logo = Image.open(BytesIO(response.content))

with st.sidebar:
    st.image(logo, use_column_width=True)
    page = st.radio("Navigate", ["Home", "About Us", "Chess"])

# Home Page
if page == "Home":
    st.title("Welcome to Chess Legends ♟️")
    st.write("""
        We offer personalized online chess coaching from experienced youth tournament players.
        
        - Weekend group sessions  
        - USCF tournament preparation  
        - Opening/Endgame/Thematic tactics  
    """)

# About Us Page
elif page == "About Us":
    st.title("Meet Our Coaches")

    col1, col2 = st.columns(2)

    with col1:
        shouri_url = "https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png"
        response1 = requests.get(shouri_url)
        shouri_img = Image.open(BytesIO(response1.content))
        st.image(shouri_img, caption="Shouri Mosaaliganti (USCF 1700)", use_column_width=True)

        st.markdown("""
        Hi, I’m **Shouri**! I’m a 14-year-old chess player with a current USCF rating of 1700 and a deep love for the game.
        I’ve played in over 180 chess tournaments, gaining valuable experience and learning from every match.

        In addition to competing, I also work as a part-time chess coach, helping students strengthen their fundamentals,
        think more critically, and build confidence at the board. I enjoy teaching players of all levels and sharing the excitement 
        and beauty of the game.
        """)

  col1, col2 = st.columns(2)

with col1:
    shouri_url = "https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png"
    response1 = requests.get(shouri_url)
    shouri_img = Image.open(BytesIO(response1.content))
    st.image(shouri_img, caption="Shouri Mosaliganti (USCF 1700)", use_column_width=True)
    st.markdown("""
    Hi, I’m **Shouri**! I’m a 14-year-old chess player with a current USCF rating of 1700 and a deep love for the game.
    I’ve played in over 180 chess tournaments, gaining valuable experience and learning from every match.

    In addition to competing, I also work as a part-time chess coach, helping students strengthen their fundamentals,
    think more critically, and build confidence at the board. I enjoy teaching players of all levels and sharing the excitement
    and beauty of the game.
    """)

with col2:
    dhairya_url = "https://i.postimg.cc/5yYQhDY7/Untitled-design-2025-07-02-T093341-074.png"
    response2 = requests.get(dhairya_url)
    dhairya_img = Image.open(BytesIO(response2.content))
    st.image(dhairya_img, caption="Dhairya Mehta (USCF 2150)", use_column_width=True)
    st.markdown("""
    My name is Dhairya Mehta, and I’m a 14-year-old chess player with a deep passion for the game.
    I currently hold a USCF rating of 2150 and have competed in over 150 tournaments across the country.

    In addition to playing competitively, I enjoy teaching others and sharing what I’ve learned.
    I’ve run a chess summer camp, where I coached younger players in a fun and supportive environment,
    and I’ve also conducted one-on-one coaching sessions with students looking to improve their game.
    Whether you’re just starting out or looking to take your skills to the next level,
    I’m excited to help you grow and enjoy the game as much as I do.
    """)
