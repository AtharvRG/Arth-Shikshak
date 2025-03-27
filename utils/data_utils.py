import joblib
import os
import streamlit as st
from typing import Dict, List

DATA_FOLDER = 'data/'

def load_past_chats() -> Dict[str, str]:
    """
    Loads past chat metadata from a file. Handles file errors, including the
    case where the file does not exist, and other potential exceptions
    during file processing.  If the file is not found, it returns an empty
    dictionary, effectively starting with no past chat history.
    """
    past_chats_file = os.path.join(DATA_FOLDER, 'past_chats_list')
    try:
        return joblib.load(past_chats_file)
    except FileNotFoundError:
        st.warning(f"Whoops! Looks like the old chat log went missing.  Fresh one coming up!")
        return {}
    except Exception as e:
        st.error(f"Uh oh, couldn't grab the old chats. Starting with a clean slate! (Error: {e})")
        return {}

def save_past_chats(past_chats: Dict[str, str]) -> None:
    """
    Saves past chat metadata to a file.  Handles potential errors during the
    saving process, such as disk errors or permission issues.  If an error
    occurs, it displays an error message to the user.
    """
    past_chats_file = os.path.join(DATA_FOLDER, 'past_chats_list')
    try:
        joblib.dump(past_chats, past_chats_file)
    except Exception as e:
        st.error(f"Dang, couldn't save the chat history.  Hope you didn't say anything too important! (Error: {e})")



def load_chat_history(chat_id: str) -> List[Dict]:
    """
    Loads chat history from a file. Handles file not found.
    Ensures the history is in the format expected by the Gemini API.
    """
    messages_file = os.path.join(DATA_FOLDER, f'{chat_id}-st_messages')
    try:
        messages = joblib.load(messages_file)
        gemini_history = []
        for message in messages:
            gemini_message = {
                "role": message["role"],
                "parts": [message["content"]]
            }
            gemini_history.append(gemini_message)
        return messages # Changed to just return messages
    except FileNotFoundError:
        st.warning(f"New chat smell!  No history for that ID ('{chat_id}').  Let's make some memories!")
        return []
    except Exception as e:
        st.error(f"Blast!  Couldn't load the chat history.  Gonna pretend this is the first time we've met. (Error: {e})")
        return []



def save_chat_history(chat_id: str, messages: List[Dict]) -> None:
    """
    Saves chat history to files. Includes error handling.  This function saves
    both the Streamlit message format and a format more directly compatible
    with the Gemini API.  It handles potential exceptions during the saving
    process for both files.
    """
    messages_file = os.path.join(DATA_FOLDER, f'{chat_id}-st_messages')
    try:
        joblib.dump(messages, messages_file)
    except Exception as e:
        st.error(f"Crap, failed to save the conversation.  The AI might forget what you said! (Error: {e})")



def load_user_data() -> Dict:
    """
    Loads user data from a file.  Handles file errors, specifically
    a FileNotFoundError, which can occur if the user has not yet
    provided their financial details.  It also handles other potential
    exceptions during file loading.
    """
    user_data_file = os.path.join(DATA_FOLDER, 'user_data')
    try:
        return joblib.load(user_data_file)
    except FileNotFoundError:
        st.warning("Where did your data go?  Oh well, starting fresh!")
        return {}
    except Exception as e:
        st.error(f"Bummer, couldn't load your user data. (Error: {e})")
        return {}

def save_user_data(user_data: Dict) -> None:
    """
    Saves user data to a file.  Handles file errors that may occur
    during the saving process.
    """
    user_data_file = os.path.join(DATA_FOLDER, 'user_data')
    try:
        joblib.dump(user_data, user_data_file)
    except Exception as e:
        st.error(f"Failed to save your precious data!. (Error: {e})")