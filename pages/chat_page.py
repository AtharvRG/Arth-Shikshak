import streamlit as st
from utils import data_utils, model_utils
import time
import os
from typing import List, Dict

DEFAULT_CHAT_TITLE = "New Chat"

def show_chat_page():
    """
    Displays the chat page, where the user interacts with the Gemini-powered
    financial advisor.  This page loads the chat history, initializes the
    chat model, displays previous messages, and handles user input.
    """
    chat_id = st.session_state.chat_id
    gemini_history = data_utils.load_chat_history(chat_id)
    model, chat = model_utils.initialize_chat_model(gemini_history, st.session_state.user_data)
    if chat is None:
        st.stop()

    st.session_state.chat = chat
    st.session_state.gemini_history = gemini_history

    messages = []
    for message in gemini_history:
        # Check if 'parts' key exists, if not, assume the message *is* the content.
        if 'parts' in message:
            content = message['parts'][0]
        else:
            content = message['content']
        model_utils.display_message(message['role'], content, message.get('avatar'))
        messages.append({'role': message['role'], 'content': content})

    if prompt := st.chat_input("Spill the beans... about your monee...eey...Financial doubts!"):
        response_text = model_utils.handle_user_input(prompt, st.session_state.chat, messages)

        if st.session_state.selected_chat_title == DEFAULT_CHAT_TITLE:
            new_chat_title = model_utils.generate_chat_title(prompt, st.session_state.chat)
            past_chats = data_utils.load_past_chats()
            past_chats[st.session_state.chat_id] = new_chat_title
            data_utils.save_past_chats(past_chats)
            st.session_state.selected_chat_title = new_chat_title

        data_utils.save_chat_history(st.session_state.chat_id, messages)
        st.rerun()
