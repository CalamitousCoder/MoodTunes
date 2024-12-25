import time as builtin_time
import Utils
import SentimentAnalyzer
import SpotifyMethods
import streamlit as st

st.set_page_config(page_title="Vibe Checker", layout="centered")
def main():
    # CSS for styling the container
    st.markdown(
        """
        <style>
        /* Reduce margins for the whole page */
        body {
            margin: 0;
            padding: 0;
        }
        /* Main container */
        .center-box {
        }
        .content-box {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        /* Styling for the bottom box */
        .bottom-box {
            height: 100vh;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main container with image and text elements
    st.markdown('<div class="center-box" id="vibe-section">', unsafe_allow_html=True)

    # Display the image in the center
    st.image("BoomBoxBros.gif", caption=None, use_container_width=True)

    # Content box for text and inputs
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
    # Add text and input elements
    st.write("### What’s your vibe right now?")
    currVibe = st.text_input("Describe your vibe:")

    if currVibe:
        st.write(f"You described your vibe as: **{currVibe}**")


if __name__ == "__main__":
    main()
