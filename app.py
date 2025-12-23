import streamlit as st
import pandas as pd
import data_manager as dm
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.set_page_config(page_title="ExpenseBuddy Clone", page_icon="💰", layout="wide")
st.title("💰 My Personal Finance Dashboard")

# --- SIDEBAR (Input Form) ---
st.sidebar.header("➕ Add New Expense")
with st.sidebar.form("expense_form", clear_on_submit=True):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Rent", "Entertainment", "Bills", "Other"])
    amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        dm.add_expense(date, category, amount, description)
        st.success("Expense Added!")

# --- MAIN DASHBOARD ---
df = dm.load_data()

if not df.empty:
    # 1. Top Metrics
    total_spent = df["Amount"].sum()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Spending", f"${total_spent:.2f}")
    col1.metric("Transaction Count", len(df))
    
    # 2. Charts & Data
    col_chart, col_data = st.columns([2, 3]) # Chart takes 40%, Data takes 60%
    
    with col_chart:
        st.subheader("Spending by Category")
        # Group data for the pie chart
        chart_data = df.groupby("Category")["Amount"].sum()
        fig, ax = plt.subplots()
        ax.pie(chart_data, labels=chart_data.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal') 
        st.pyplot(fig)

    with col_data:
        st.subheader("Recent Transactions")
        st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)

else:
    st.info("No expenses yet. Add one from the sidebar!")