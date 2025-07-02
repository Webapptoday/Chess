import streamlit as st

# Set page config
st.set_page_config(page_title="Student Chess Network", layout="wide")

# Blue theme background
st.markdown("""
    <style>
    body {
        background-color: #e0f0ff;
    }
    .section {
        padding: 2rem 1rem;
    }
    h1, h2, h3 {
        color: #003366;
    }
    .nav {
        background-color: #0077cc;
        padding: 1rem;
        text-align: center;
    }
    .nav a {
        color: white;
        margin: 0 15px;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<div class="nav">
    <a href="#home">Home</a>
    <a href="#about-us">About Us</a>
    <a href="#coaches">Coaches</a>
    <a href="#pricing">Pricing</a>
    <a href="#why-us">WHY US</a>
    <a href="#book-now">Book Now</a>
</div>
""", unsafe_allow_html=True)

# HOME Section
st.markdown('<h1 id="home">Student Chess Network</h1>', unsafe_allow_html=True)
st.subheader("For quality, affordable and genuine chess coaching for kids of all levels")

# ABOUT US
st.markdown('<h2 id="about-us">About Us</h2>', unsafe_allow_html=True)
st.write("""
Welcome to Student Chess Network! We offer personalized and flexible chess coaching for kids of all levels.

**What We Offer:**
- Weekly 1-on-1 coaching
- Weekend group sessions
- USCF tournament preparation
- Opening/Endgame/Thematic tactics
""")

# COACHES
st.markdown('<h2 id="coaches">Meet Our Coaches</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.image("https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png", 
             caption="Dhairya Mehta (USCF 2150)", use_column_width=True)
    st.write("Over 150 tournaments • Summer camp coach")

with col2:
    st.image("https://i.postimg.cc/5yYQhDY7/Untitled-design-2025-07-02-T093341-074.png", 
             caption="Shouri Mosaliganti (USCF 1700)", use_column_width=True)
    st.write("180+ tournaments • Experienced youth coach")


# PRICING
st.markdown('<h2 id="pricing">Pricing</h2>', unsafe_allow_html=True)
st.write("""
- **Online Coaching**: $25/hour
- **In-Person Coaching**: $40/hour
- **Group Lessons**: $30/hour per student
""")

# WHY US
st.markdown('<h2 id="why-us">Why Us?</h2>', unsafe_allow_html=True)
st.markdown("""
- ✅ Affordable rates for all families  
- ✅ Coaches with deep tournament experience  
- ✅ Personalized weekly progress tracking  
- ✅ Flexible scheduling for busy kids  
- ✅ Proven track record with student improvement
""")

# BOOK NOW
st.markdown('<h2 id="book-now">Book a Class</h2>', unsafe_allow_html=True)
st.markdown("""
Want to start your journey?  
👉 [Fill out our booking form](https://docs.google.com/forms/d/1ofBOQYqdp8hRGIYKzPic2-sQIlsOokO9gq6PBzT7sxg)  
We’ll get back to you within 24 hours!
""")

st.markdown("---")
st.caption("© 2025 Student Chess Network")
