import streamlit as st
from PIL import Image

st.set_page_config(page_title="I'm Sorry ❤️", page_icon="💌", layout="centered")

if 'forgiven' not in st.session_state:
    st.session_state.forgiven = False

# Confetti function
def fire_confetti():
    st.balloons()

if not st.session_state.forgiven:
    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
        st.markdown("<h1 style='margin-bottom:0.1rem'>I'M SORRY</h1>", unsafe_allow_html=True)
        st.markdown("<h5 style='margin-top:0.0rem;color:#28a745'>Caslee please forgive me for not paying attention to you. Pretty please.</h3>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.write("---")
        st.subheader("Forgive Me? 💔 → 💖")

        forgive_button = st.button("💚 Forgive Me")
        not_yet_button = st.button("❌ Not Yet")

        if forgive_button:
            st.session_state.forgiven = True

        if not_yet_button:
            st.warning("Please forgive me soon 😔")

    with col2:
        # Replace the path with the full path to your picture
        image_path = r"C:\Users\kokei\Downloads\her_picture.jpg"  # <-- your file here
        img = Image.open(image_path)
        st.image(img, caption="Our son is asking as as well ❤️")

# Once forgiven, show only balloons and love message
if st.session_state.forgiven:
    fire_confetti()
    st.markdown("<h1 style='text-align:center; color:#28a745;'>Yay! I love you ❤️</h1>", unsafe_allow_html=True)
