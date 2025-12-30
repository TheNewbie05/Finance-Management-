# file_manager.py
import pandas as pd
import os

CSV_FILE = os.path.join("data", "expenses.csv")

def ensure_storage_exists():
    """Creates the data folder and file if they don't exist."""
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(CSV_FILE, index=False)

def save_expense(expense_obj):
    """Appends a single expense object to the CSV."""
    ensure_storage_exists()
    df = pd.DataFrame([expense_obj.to_list()])
    df.to_csv(CSV_FILE, mode='a', header=False, index=False)

def load_expenses():
    """Reads all expenses from the CSV."""
    ensure_storage_exists()
    return pd.read_csv(CSV_FILE)