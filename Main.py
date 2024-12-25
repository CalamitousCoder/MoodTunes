import time as builtin_time
import SentimentAnalyzer
import SpotifyMethods
import streamlit as st
## to do handle outliers and pretty up with comments
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

    # Initialize variables
hasPreference = False
answer = None  # Initialize answer as None

if currVibe:
        # Integrating the backend logic for analyzing vibe
        wordsList = SentimentAnalyzer.getWords(currVibe)
        areOutliers, particFeeling = SentimentAnalyzer.findOutlierFeelings(wordsList)

        if not areOutliers:
            # If not an outlier, process normally
            isCertain, currVibe, clarityMessage = SentimentAnalyzer.vibeChecker(currVibe)
            if(not isCertain ):
                extraInfo = st.text_input(clarityMessage)

                clarityMessage2, currVibe = SentimentAnalyzer.clarifyVibe(extraInfo,currVibe)
            st.write(f"Your vibe has been categorized as: **{currVibe}**")
        else:
            # Handle outlier feelings
            currVibe = particFeeling
            st.write(f"Your vibe seems to be an outlier, interpreted as: **{currVibe}**")

        # Display the final result
        st.write(f"I got your vibe as: **{currVibe}**")
        currGoodVibes = currVibe == "happy" or currVibe == "upbeat"
        currBadVibes = True if not currGoodVibes else False

        # Ask for music genre preference
        st.write(f"List a genre of music you'd like to hear")
        userGenre = st.text_input("If you have no preference type 'any'")

        # Check if user has a preference
        hasPreference = userGenre.lower() != "any"

        # Create a selectbox for user to choose an option
        answer = st.selectbox(
            'Would you like to:',
            ['Intensify Vibe', 'Keep Vibe Going', 'Balance Mood', 'Shake Things Up A Little', 'Feel Whiplash']
        )

        # Handle the selected option only if answer is not None
        if answer and not areOutliers:
            match answer:
                case 'Intensify Vibe':
                    if hasPreference:
                         if(currGoodVibes):
                            playListName, playlistUrl, =  SpotifyMethods.genreSearch("ultimate feel good rap", userGenre)
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                         else:
                            playListName, playlistUrl, =  SpotifyMethods.genreSearch("super depressing", userGenre)
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                             
                    else:
                        if(currGoodVibes):
                            playListName, playlistUrl, =  SpotifyMethods.basicSearch("ultimate feel good")
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                        else:
                            playListName, playlistUrl, =  SpotifyMethods.basicSearch("super depressing")
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)

                case 'Keep Vibe Going':
                    if hasPreference:
                        playListName, playlistUrl, =  SpotifyMethods.genreSearch(currVibe, userGenre)
                        st.write("We think you'll like this playlist: " + playListName)
                        st.write(playlistUrl)
                    else:
                        playListName, playlistUrl, =  SpotifyMethods.basicSearch(currVibe)
                        st.write("We think you'll like this playlist: " + playListName)
                        st.write(playlistUrl)
                case 'Balance Mood':
                    if hasPreference:
                        playListName, playlistUrl, =  SpotifyMethods.genreSearch("chill", userGenre)
                        st.write("We think you'll like this playlist: " + playListName)
                        st.write(playlistUrl)
                    else:
                        playListName, playlistUrl, =  SpotifyMethods.basicSearch("chill")
                        st.write("We think you'll like this playlist: " + playListName)
                        st.write(playlistUrl)
                case 'Shake Things Up A Little':
                    if hasPreference:
                         if(currGoodVibes):
                            playListName, playlistUrl, =  SpotifyMethods.genreSearch("sad", userGenre)
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                         else:
                            playListName, playlistUrl, =  SpotifyMethods.genreSearch("happy", userGenre)
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                             
                    else:
                        if(currGoodVibes):
                            playListName, playlistUrl, =  SpotifyMethods.basicSearch("sad")
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                        else:
                            playListName, playlistUrl, =  SpotifyMethods.basicSearch("happy")
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                    
                case 'Feel Whiplash':
                    if hasPreference:
                         if(not currGoodVibes):
                            playListName, playlistUrl, =  SpotifyMethods.genreSearch("ultimate feel good", userGenre)
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                         else:
                            playListName, playlistUrl, =  SpotifyMethods.genreSearch("super depressing", userGenre)
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                             
                    else:
                        if(not currGoodVibes):
                            playListName, playlistUrl, =  SpotifyMethods.basicSearch("ultimate feel good")
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)
                        else:
                            playListName, playlistUrl, =  SpotifyMethods.basicSearch("super depressing")
                            st.write("We think you'll like this playlist: " + playListName)
                            st.write(playlistUrl)                   

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
if __name__ == "__main__": main() 