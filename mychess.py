import streamlit as st

st.set_page_config(page_title="Chess Legends", layout="wide")
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

        with col1:
            st.image(
                "https://i.postimg.cc/5yYQhDY7/Untitled-design-2025-07-02-T093341-074.png",
                caption="Dhairya Mehta (USCF 2150)",
                use_container_width=True
            )
            st.write("Over 150 tournaments • Summer camp coach")

        with col2:
            st.image(
                "https://i.postimg.cc/d3bZwnGq/Untitled-design-2025-07-02-T093312-238.png",
                caption="Shouri Mosaliganti (USCF 1700)",
                use_container_width=True
            )
            st.write("180+ tournaments • Experienced youth coach")

# Pricing Section
elif page == "Pricing":
    with st.expander("Pricing", expanded=True):
        st.write("🏷️ **$25/hr - Group lessons**")
        st.write("🎯 **$40/hr - Private coaching**")
        st.write("Discounts available for bulk bookings.")

# Contact Section
elif page == "Contact":
    with st.expander("Contact Us", expanded=True):
        st.write("📧 chesslegends@example.com")
        st.write("📍 Based in Massachusetts, USA")
