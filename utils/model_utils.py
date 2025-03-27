import google.generativeai as genai
import streamlit as st
from typing import List, Dict, Optional
import time
# Constants
MODEL_ROLE = 'Arth Shikshak'
MAX_CHAT_LENGTH = 50
DEFAULT_CHAT_TITLE = "New Chat"
AI_AVATAR_ICON = '💰'
FINANCIAL_ADVICE_PROMPT = """You are a financial advisor. Your responses should be limited to providing financial advice,
guidance, and education. Do not discuss topics outside of finance, such as personal opinions,
general knowledge, or unrelated subjects. Focus on providing accurate and helpful information
related to investments, budgeting, saving, debt management, retirement planning, and other
financial matters.  All monetary values should be expressed in Indian Rupees (₹). When providing advice, consider the user's financial situation:
- Annual Income: ₹{annual_income}
- Current Savings: ₹{current_savings}
- Housing Expenses: ₹{housing}
- Food Expenses: ₹{food}
- Transportation Expenses: ₹{transportation}
- Utilities Expenses: ₹{utilities}
- Other Expenses: ₹{other}
"""

def initialize_chat_model(history: List[Dict], user_data: Dict) -> genai.GenerativeModel:
    """
    Initializes the Gemini model and chat session, handling potential errors
    that may occur during the model initialization process.  This includes
    setting up the chat history with the initial financial advice prompt,
    contextualized with the user's financial data.
    """
    try:
        prompt_with_context = FINANCIAL_ADVICE_PROMPT.format(
            annual_income=user_data.get("annual_income", 0),
            current_savings=user_data.get("current_savings", 0),
            housing=user_data.get("housing", 0),
            food=user_data.get("food", 0),
            transportation=user_data.get("transportation", 0),
            utilities=user_data.get("utilities", 0),
            other=user_data.get("other", 0),
        )

        model = genai.GenerativeModel('gemini-2.0-flash')
        chat = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [prompt_with_context],
                }
            ]
        )
        return model, chat
    except Exception as e:
        st.error(f"Well, this is awkward.  The AI is refusing to wake up.  (Error: {e})")
        return None, None



def generate_chat_title(prompt: str, chat: genai.ChatSession) -> str:
    """
    Generates a title for the chat based on the initial prompt provided
    by the user.  This title is used to help the user identify and
    recall past chat sessions.
    """
    try:
        title_prompt = f"Create a concise title (max {MAX_CHAT_LENGTH} characters) for this financial education chat: '{prompt}'. Do not include any preamble or salutations. Just the title."
        response = chat.send_message(title_prompt)
        title = response.text.strip()
        return title[:MAX_CHAT_LENGTH]
    except Exception as e:
        st.error(f"AI had a brain fart trying to name the chat.  Going with the boring default. (Error: {e})")
        return DEFAULT_CHAT_TITLE
    
def handle_user_input(prompt: str, chat: genai.ChatSession, messages: List[Dict]) -> str:
    """
    Handles user input, sends it to the model, and returns the response.
    Displays the user's message, appends it to the message list, sends the
    prompt to the Gemini chat model, and then displays the model's
    response in a streaming fashion.
    """
    display_message('user', prompt, avatar=AI_AVATAR_ICON)
    messages.append({'role': 'user', 'content': prompt})

    try:
        response = chat.send_message(prompt, stream=True)
        full_response = ''
        message_placeholder = st.empty()
        for chunk in response:
            full_response += chunk.text
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.02)

        message_placeholder.markdown(full_response)
        messages.append({'role': MODEL_ROLE, 'content': full_response, 'avatar': AI_AVATAR_ICON})
        return full_response

    except Exception as e:
        error_message = f"The AI didn't quite get that.  Lost in translation! (Error: {e})"
        st.error(error_message)
        messages.append({'role': MODEL_ROLE, 'content': error_message, 'avatar': AI_AVATAR_ICON})
        return error_message
    
def display_message(role: str, content: str, avatar: Optional[str] = None) -> None:
    """
    Displays a chat message with consistent styling and error handling. This
    function uses the st.chat_message context manager to display the message
    with the appropriate role and avatar.  It also includes error handling
    to catch any exceptions that may occur during the display process.
    """
    try:
        with st.chat_message(name=role, avatar=avatar):
            st.markdown(content)
    except Exception as e:
        st.error(f"Double crap! Something went wrong while displaying the message.  (Error: {e}).  Role = {role}, Content = {content}")