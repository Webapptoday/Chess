import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="SCN", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .stApp { background-color: #e6f2ff; }
        .full-width-img img { width: 100% !important; height: auto; }
        .sidebar .sidebar-content { padding-top: 30px; }
        .block-container { padding-top: 2rem; }
        .center { text-align: center; }
        .benefit-icon { font-size: 24px; padding-right: 10px; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://i.postimg.cc/vBZcwTSH/Chat-GPT-Image-Jul-2-2025-10-04-14-AM.png", width=150)
    page = st.radio("Navigate", [
        "Home", "About Us", "Why Chess is the Best Move", "Summer Camp", "Motivation", "Book a Class"
    ])

# --- Home ---
if page == "Home":
    st.title("Welcome to SCN")
    st.subheader("Student Chess Network")
    st.markdown("""
    We offer high-quality, student-led chess coaching for all levels:
    - One-on-one personalized sessions  
    - Group classes with tactical and strategic focus  
    - USCF tournament preparation  
    - Opening/Endgame/Thematic tactics  
    """)

    img = Image.open(BytesIO(requests.get("https://i.postimg.cc/8C32BPfn/image-2.png").content))
    st.image(img, caption="SCN Chess Coaching", use_container_width=True)

# --- About Us ---
elif page == "About Us":
    st.title("Meet the Coaches Behind SCN")
    st.markdown("""
    Our student coaches are dedicated to helping young players grow and thrive.  
    Get to know the minds leading your chess journey:
    """)

    col1, col2 = st.columns(2)

    with col1:
        dhairya_img = Image.open(BytesIO(requests.get("https://i.postimg.cc/5yYQhDY7/Untitled-design-2025-07-02-T093341-074.png").content))
        st.image(dhairya_img, caption="Dhairya Mehta (USCF 2150)", use_container_width=True)
        st.markdown("""
**Dhairya Mehta**  
📧 [mehtadhairya11@gmail.com](mailto:mehtadhairya11@gmail.com)  
📞 857-832-1547  
🗓️ [Book a Trial](https://calendly.com/your-trial-link)

I'm a 14-year-old competitive player with 150+ tournaments under my belt and a 2150 rating.  
My passion lies in helping others enjoy the game as much as I do. Let's grow your skills together!
""")

    with col2:
        shouri_img = Image.open(BytesIO(requests.get("https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png").content))
        st.image(shouri_img, caption="Shouri Mosaliganti (USCF 1700)", use_container_width=True)
        st.markdown("""
**Shouri Mosaliganti**  
📧 [28stu521@lexingtonma.org](mailto:28stu521@lexingtonma.org)  
📞 857-214-9563  
🗓️ [Book a Trial](https://calendly.com/your-trial-link)

I'm a 14-year-old coach and chess enthusiast with over 180 tournaments of experience.  
I specialize in teaching tactics, confidence-building, and joy through chess.
""")

# --- Why Chess Is the Best Move ---
elif page == "Why Chess is the Best Move":
    st.title("Why Chess is the Best Move")

    img = Image.open(BytesIO(requests.get("https://i.postimg.cc/J0HS2wZ4/image.png").content))
    st.image(img, use_container_width=True)

    st.markdown("### What Chess Builds:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🧠 **Critical Thinking**  \nPlan ahead, adapt, and evaluate.")
        st.markdown("🎯 **Focus**  \nDevelop laser-like attention.")
        st.markdown("💡 **Creativity**  \nFind unexpected and elegant solutions.")
    with col2:
        st.markdown("🧮 **Problem Solving**  \nTrain logic and strategy.")
        st.markdown("🗺️ **Planning**  \nUnderstand cause and effect.")
        st.markdown("📚 **Memory**  \nImprove recall and pattern recognition.")

    st.markdown("### 👉 Ready to develop these skills?")
    st.link_button("Join a Class Today", "https://your-signup-form.com")

# --- Summer Camp ---
elif page == "Summer Camp":
    st.title("Summer Chess Camp 2025")
    flyer_url = "https://i.postimg.cc/vBL9yDy4/HOPKINGTON-CHURCH-1.png"
    flyer_response = requests.get(flyer_url)
    flyer_image = Image.open(BytesIO(flyer_response.content))

    st.markdown('<div class="full-width-img">', unsafe_allow_html=True)
    st.image(flyer_image, caption="Hopkinton Chess Camp 2025", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.header("Pricing")
    st.markdown("""
- **$100** for 4 group sessions  
- **$30** for 1 class  
- 🎁 Free 1-on-1 trial class with every camper!
    """)

    st.link_button("Register Now", "https://forms.gle/fvagn29qQTBpXq1P6")



    st.subheader("Testimonials")
    st.info("“The camp was amazing! My son loved it and learned so much.” – Parent, 2023")

# --- Motivation ---
elif page == "Motivation":
    st.title("Motivation")
    img = Image.open(BytesIO(requests.get("https://i.postimg.cc/13MP6QKL/image-1.png").content))
    st.markdown('<div class="full-width-img">', unsafe_allow_html=True)
    st.image(img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
### Why We Coach
We believe chess is more than a game — it’s a mindset. It teaches us patience, strategy, confidence, and persistence.

> “Chess has taught me patience and resilience.” — **Dhairya**
    """)

# --- Book a Class ---
elif page == "Book a Class":
    st.title("Book a Class")

    st.markdown("""
### Options:
- 🧒 **Beginner Class** – Intro to chess fundamentals
- ♟️ **Intermediate Strategy** – Opening, middlegame & endgame
- 🔥 **Tactics Training** – Puzzles and competitive scenarios

Use our form or book directly below.
    """)

    st.link_button("Sign Up via Google Form", "https://forms.gle/fvagn29qQTBpXq1P6")

    st.subheader("Or reserve using our calendar:")
    st.markdown("""
<iframe src="https://calendly.com/your-calendar-link" width="100%" height="600" frameborder="0"></iframe>
    """, unsafe_allow_html=True)
