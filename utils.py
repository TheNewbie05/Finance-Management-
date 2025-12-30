import streamlit as st
from datetime import datetime

def validate_data(amount, description):
    """Ensures input is valid before saving."""
    if amount <= 0:
        st.error("Please enter an amount greater than 0.")
        return False
    if not description.strip():
        st.warning("Please provide a description.")
        return False
    return True

def format_currency(value):
    """Formats a number as currency string."""
    return f"${value:,.2f}"

def get_current_month():
    """Returns the name of the current month (e.g., 'December 2025')."""
    return datetime.now().strftime("%B %Y")