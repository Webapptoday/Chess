import streamlit as st

st.set_page_config(page_title="Chess Legends", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 2rem;
        }
        .stImage > img {
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Coaches", "Pricing", "Contact"])

# About Section
if page == "About":
    st.title("Welcome to Chess Legends")
    st.write("Train with top-rated youth players and experienced coaches. Build your tactics, strategy, and confidence over the board.")

# Coaches Section
elif page == "Coaches":
    with st.expander("Meet Our Coaches", expanded=True):
        col1, col2 = st.columns(2)

        # Dhairya (left)
        with col1:
            st.image(
                "https://i.postimg.cc/5yYQhDY7/Untitled-design-2025-07-02-T093341-074.png",
                caption="Dhairya Mehta (USCF 2150)",
                use_container_width=True
            )
            st.write("Over 150 tournaments • Summer camp coach")
            st.markdown("""
            My name is Dhairya Mehta, and I’m a 14-year-old chess player with a deep passion for the game.  
            I currently hold a USCF rating of 2150 and have competed in over 150 tournaments across the country.  
            Chess has been a big part of my life for many years, and I love both the strategy and the challenge it brings.

            In addition to playing competitively, I enjoy teaching others and sharing what I’ve learned.  
            I’ve run a chess summer camp, where I coached younger players in a fun and supportive environment,  
            and I’ve also conducted one-on-one coaching sessions with students looking to improve their game.

            Whether you’re just starting out or looking to take your skills to the next level,  
            I’m excited to help you grow and enjoy the game as much as I do.
            """)

        # Shouri (right)
        with col2:
            st.image(
                "https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png",
                caption="Shouri Mosaliganti (USCF 1700)",
                use_container_width=True
            )
            st.write("180+ tournaments • Experienced youth coach")
            st.markdown("""
            Hi, I’m Shouri! I’m a 14-year-old chess player with a current USCF rating of 1700  
            and a deep love for the game. I’ve played in over 180 chess tournaments,  
            gaining valuable experience and learning from every match.

            Whether it’s sharp tactics or long strategic battles,  
            I enjoy all aspects of chess and am always striving to improve.

            In addition to competing, I also work as a part-time chess coach,  
            helping students strengthen their fundamentals, think more critically,  
            and build confidence at the board.

            I enjoy teaching players of all levels and sharing the excitement and beauty of the game.
            """)

# Pricing Section
elif page == "Pricing":
    with st.expander("Pricing", expanded=True):
        st.write("🏷️ **$25/hr - Group lessons**")
        st.write("🎯 **$40/hr - Private coaching**")
        st.write("💡 Discounts available for bulk bookings.")

# Contact Section
elif page == "Contact":
    with st.expander("Contact Us", expanded=True):
        st.write("📧 chesslegends@example.com")
        st.write("📍 Based in Massachusetts, USA")
