import pandas as pd
import os
from datetime import datetime

CSV_FILE = 'expenses.csv'

def initialize_data():
    """Creates the CSV if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(CSV_FILE, index=False)

def load_data():
    """Loads expenses into a Pandas DataFrame."""
    initialize_data()
    return pd.read_csv(CSV_FILE)

def add_expense(date, category, amount, description):
    """Adds a new row to the CSV."""
    new_data = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount],
        "Description": [description]
    })
    # Append to existing file without reading the whole thing
    new_data.to_csv(CSV_FILE, mode='a', header=not os.path.exists(CSV_FILE), index=False)