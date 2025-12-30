import pandas as pd
import os

CSV_FILE = "expenses.csv"

def init_file():
    """Creates the CSV file if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(CSV_FILE, index=False)

def load_expenses():
    """Loads data from the CSV file."""
    init_file()  # Ensure file exists first
    try:
        return pd.read_csv(CSV_FILE)
    except Exception:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

def save_expense(expense):
    """Saves a new expense to the CSV file."""
    init_file()  # Ensure file exists first
    
    # Convert the expense object to a DataFrame
    new_data = pd.DataFrame([expense.to_dict()])
    
    # Append it to the existing CSV file
    # mode='a' means append (don't overwrite)
    # header=False means don't write the column names again
    new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)