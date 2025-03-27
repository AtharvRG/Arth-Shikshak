import streamlit as st
from utils import data_utils
import os

DATA_FOLDER = 'data/'

def show_input_page():
    """
    Displays the input page, where the user enters their financial details.
    This page includes input fields for annual income, current savings, and
    various expenses.  It checks if the user data file already exists and
    skips the input fields if it does.
    """
    if "user_data" not in st.session_state:
        st.session_state.user_data = data_utils.load_user_data()
    st.header("Enter Your Financial Details")
    #check if data exists
    if not os.path.exists(os.path.join(DATA_FOLDER, 'user_data')):
        st.session_state.user_data["annual_income"] = st.number_input("Annual Income (₹):", min_value=0, value=st.session_state.user_data.get("annual_income", 0))
        st.session_state.user_data["current_savings"] = st.number_input("Current Savings (₹):", min_value=0, value=st.session_state.user_data.get("current_savings", 0))
        st.session_state.user_data["housing"] = st.number_input("Housing Expenses (₹):", min_value=0, value=st.session_state.user_data.get("housing", 0))
        st.session_state.user_data["food"] = st.number_input("Food Expenses (₹):", min_value=0, value=st.session_state.user_data.get("food", 0))
        st.session_state.user_data["transportation"] = st.number_input("Transportation Expenses (₹):", min_value=0, value=st.session_state.get("transportation", 0))
        st.session_state.user_data["utilities"] = st.number_input("Utilities Expenses (₹):", min_value=0, value=st.session_state.user_data.get("utilities", 0))
        st.session_state.user_data["other"] = st.number_input("Other Expenses (₹):", min_value=0, value=st.session_state.user_data.get("other", 0))
        if st.button("Save Details"):
            st.success("Gotcha!  Your financial deets are locked in.  Let's talk money!")
            data_utils.save_user_data(st.session_state.user_data)
            st.session_state.page = "chat"
            st.rerun()
    else:
        st.session_state.page = "chat"
        st.rerun()