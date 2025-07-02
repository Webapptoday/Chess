import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Apply custom background and logo styles
st.set_page_config(page_title="SCN", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #e6f2ff;
        }
        .full-width-img img {
            width: 100% !important;
            height: auto;
        }
        .sidebar .sidebar-content {
            padding-top: 30px;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar logo and navigation
with st.sidebar:
    st.image("https://i.postimg.cc/vBZcwTSH/Chat-GPT-Image-Jul-2-2025-10-04-14-AM.png", width=150)
    page = st.radio("Navigate", ["Home", "About Us", "Chess", "Summer Camp"])

# -----------------------
# HOME PAGE
# -----------------------
if page == "Home":
    st.title("Welcome to SCN")
    st.subheader("Student Chess Network")
    st.write("""
    We offer high-quality, student-led chess coaching for all levels:
    - One-on-one personalized sessions  
    - Group classes with tactical and strategic focus  
    - Weekend group sessions  
    - USCF tournament preparation  
    - Opening/Endgame/Thematic tactics  
    """)

# -----------------------
# ABOUT US PAGE
# -----------------------
elif page == "About Us":
    st.title("Meet Our Coaches")

    col1, col2 = st.columns(2)

    with col1:
        dhairya_url = "https://i.postimg.cc/5yYQhDY7/Untitled-design-2025-07-02-T093341-074.png"
        response1 = requests.get(dhairya_url)
        dhairya_img = Image.open(BytesIO(response1.content))
        st.image(dhairya_img, caption="Dhairya Mehta (USCF 2150)", use_column_width=True)

        st.markdown("""
        **Dhairya Mehta**  
        📧 mehtadhairya11@gmail.com  
        📞 857-832-1547  
        
        My name is Dhairya Mehta, and I’m a 14-year-old chess player with a deep passion for the game.  
        I currently hold a USCF rating of 2150 and have competed in over 150 tournaments across the country.

        In addition to playing competitively, I enjoy teaching others and sharing what I’ve learned.  
        I’ve run a chess summer camp, where I coached younger players in a fun and supportive environment,  
        and I’ve also conducted one-on-one coaching sessions with students looking to improve their game.  
        Whether you’re just starting out or looking to take your skills to the next level,  
        I’m excited to help you grow and enjoy the game as much as I do.
        """)

    with col2:
        shouri_url = "https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png"
        response2 = requests.get(shouri_url)
        shouri_img = Image.open(BytesIO(response2.content))
        st.image(shouri_img, caption="Shouri Mosaliganti (USCF 1700)", use_column_width=True)

        st.markdown("""
        **Shouri Mosaliganti**  
        📧 28stu521@lexingtonma.org  
        📞 857-214-9563  

        Hi, I’m Shouri! I’m a 14-year-old chess player with a current USCF rating of 1700 and a deep love for the game.  
        I’ve played in over 180 chess tournaments, gaining valuable experience and learning from every match.  

        Whether it’s sharp tactics or long strategic battles, I enjoy all aspects of chess and am always striving to improve.  
        In addition to competing, I also work as a part-time chess coach, helping students strengthen their fundamentals,  
        think more critically, and build confidence at the board.  
        I enjoy teaching players of all levels and sharing the excitement and beauty of the game.
        """)

# -----------------------
# CHESS PAGE
# -----------------------
elif page == "Chess":
    st.title("Why Learn Chess?")
    st.write("""
    Learning to play chess offers students an opportunity to sharpen their intellect and develop essential life skills.  
    The game is a powerful tool for enhancing critical thinking, strategic planning, and decision-making under pressure.  
    Each move requires thorough analysis and foresight, encouraging players to weigh consequences and anticipate outcomes.

    Beyond cognitive benefits, chess also fosters patience, discipline, and resilience—qualities that translate  
    to academic and personal success. As students navigate complex challenges both on and off the board,  
    chess equips them with a mindset of perseverance and ability to make wise decisions,  
    making it a valuable addition to a child’s growth.
    """)

# -----------------------
# SUMMER CAMP PAGE
# -----------------------
elif page == "Summer Camp":
    st.title("Summer Chess Camp 2025")
    flyer_url = "https://i.postimg.cc/vBL9yDy4/HOPKINGTON-CHURCH-1.png"
    flyer_response = requests.get(flyer_url)
    flyer_image = Image.open(BytesIO(flyer_response.content))

    st.markdown('<div class="full-width-img">', unsafe_allow_html=True)
    st.image(flyer_image, caption="Hopkinton Chess Camp 2025")
    st.markdown('</div>', unsafe_allow_html=True)

    st.header("Pricing")
    st.write("""
    - **$100** for 4 classes  
    - **$30** for 1 class  
    - **Bonus**: Summer camp includes a free trial 1-on-1 class!
    """)

