# Sound Track My Mood
## Short Description:
Sound Track My Mood is a web app that listens to your mood and curates a playlist based on your vibe. Users describe how they feel, and through sentiment analysis and AI, the app generates a personalized playlist recommendation from Spotify.

## Future Goals:

Complete handling of outlier emotions: I plan to refine the current sentiment analysis model to better handle outlier phrases and emotions that are not adequately processed at this stage.

## How It's Made

### Concepts used: Sentiment analysi,s API integration, Tokenization
### Key Technologies and Libraries

Streamlit: A powerful library for rapidly building interactive web applications in Python. Streamlit is used here to create the user interface and handle interactions in real-time.

TextBlob and NLTK: These libraries are used for natural language processing tasks, including sentiment analysis and tokenization. They help determine the user's mood based on their input.

## Notable Classes

### SentimientAnlyasis

This class processes the user input, performing sentiment analysis using TextBlob or NLTK to determine the user’s mood. It’s key in categorizing the mood into a scale that helps in playlist generation.


### SpotifyMethods
A class that handles all interactions with the Spotify API, including authentication, fetching track recommendations, and dealing with any API rate limits.

## Methods
###checkVibe

Uses sentiment analysis to rate the user's mood. It breaks down the input text to understand positive, negative, or neutral sentiments, allowing the app to tailor the playlist accordingly.

### findOutlierFeelings

Tokenizes the user's input to detect any unusual or outlier words that might confuse the AI. The method is essential for refining the mood detection accuracy and improving the user experience.

### genreSearch

Fetches personalized playlist recommendations based on the user's mood and genre preference. It ensures that Spotify's API is used efficiently and delivers relevant content.

genre choice and mood preference to help tailor future experiences and playlists.
## General App Flow

When the user visits the app, they are greeted with an interface that asks for their mood, prompting them to enter a description of how they feel. The input text is then tokenized and passed through a sentiment analysis model; if the input contains outlier phrases, they are flagged for improvement, but otherwise, the mood is classified (e.g., happy, sad, etc.). Following mood analysis, the app prompts the user to select a music genre they’d like to listen to, and this preference is saved. Based on the user’s mood and genre, the app generates a playlist using the Spotify API and presents it to the user. Finally, the user is shown a list of tracks, ready to listen to their personalized playlist

## Lessons Learned
First API Integration:
    Integrating the Spotify API was a challenging yet rewarding experience. It taught me about authentication flow and the limits of third-party services.

Backend and Frontend with Streamlit:
    Building a full-stack app using Streamlit was a great learning experience. It allowed me to quickly prototype the app while focusing on the AI and backend logic.

Basics of AI Fine-tuning with TextBlob and NLTK:
    Fine-tuning sentiment analysis models to accurately process various moods and outlier phrases has been an essential skill to learn.

Security and Safe Handling of Client Secrets:
    Protecting the Spotify API key and handling sensitive information securely is critical, especially when dealing with authentication systems in production.

## Known Limitations
API Access Limitations:
    Due to Spotify's restrictions, the app can currently only authenticate up to 20 users outside of the development phase. Future expansions will require an upgraded plan or alternate authentication methods.

Outlier Phrases:
    The current sentiment analysis model may misinterpret certain outlier phrases. Further development will address these issues.
