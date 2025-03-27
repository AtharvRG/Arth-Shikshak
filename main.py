import streamlit as st
from utils import data_utils, model_utils
from pages import input_page, chat_page
import time
import os
import google.generativeai as genai

# Configuration
GOOGLE_API_KEY = 'YOUR API KEY Please!'
genai.configure(api_key=GOOGLE_API_KEY)

# Constants
MODEL_ROLE = 'Arth Shikshak'
AI_AVATAR_ICON = '💰'
DATA_FOLDER = 'data/'
DEFAULT_CHAT_TITLE = "New Chat"
MAX_CHAT_LENGTH = 50

# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

def main():
    """
    Main function to run the Streamlit application.
    This function initializes the Streamlit page configuration, loads past chats,
    manages the sidebar for chat selection, and determines which page to display
    (input or chat) based on the application's state.  It serves as the central
    control point for the application flow.
    """
    st.set_page_config(page_title="Arth Shikshak Chat", page_icon=AI_AVATAR_ICON)

    past_chats = data_utils.load_past_chats()

    # --- Sidebar ---
    with st.sidebar:
        st.title("Past Chats")
        chat_options = [DEFAULT_CHAT_TITLE] + list(past_chats.values())

        if "selected_chat_title" not in st.session_state:
            st.session_state.selected_chat_title = DEFAULT_CHAT_TITLE

        selected_chat_title = st.selectbox(
            "Select a chat:",
            options=chat_options,
            index=chat_options.index(st.session_state.selected_chat_title),
        )

        if selected_chat_title == DEFAULT_CHAT_TITLE:
            chat_id = f"{time.time()}"
        else:
            chat_id = list(past_chats.keys())[chat_options.index(st.session_state.selected_chat_title) - 1]

        st.session_state.chat_id = chat_id

    # --- Main Chat Area ---
    st.title("Chat with Gemini")

    # Load user data
    if "user_data" not in st.session_state:
        st.session_state.user_data = data_utils.load_user_data()

    # Initialize page state
    if "page" not in st.session_state:
        st.session_state.page = "input"

    # User Data Input Page
    if st.session_state.page == "input":
        input_page.show_input_page()

    # Chat Page
    elif st.session_state.page == "chat":
        chat_page.show_chat_page()
        
if __name__ == "__main__":
    main()