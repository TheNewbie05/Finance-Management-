# menu.py
import streamlit as st
import file_manager as fm
import utils
from expense import Expense

def draw_sidebar():
    """Renders the input form in the sidebar."""
    st.sidebar.header("➕ Add New Expense")
    
    date = st.sidebar.date_input("Date")
    category = st.sidebar.selectbox("Category", ["Food", "Transport", "Bills", "Rent", "Other"])
    amount = st.sidebar.number_input("Amount ($)", min_value=0.0)
    desc = st.sidebar.text_input("Description")
    
    if st.sidebar.button("Save Entry"):
        if utils.validate_data(amount, desc):
            new_expense = Expense(date, category, amount, desc)
            fm.save_expense(new_expense)
            st.sidebar.success("Expense Recorded!")
            st.rerun()