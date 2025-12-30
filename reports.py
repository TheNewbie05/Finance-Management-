# reports.py
import matplotlib.pyplot as plt
import streamlit as st

def render_category_pie(df):
    """Generates a pie chart of spending by category."""
    if not df.empty:
        totals = df.groupby("Category")["Amount"].sum()
        fig, ax = plt.subplots()
        ax.pie(totals, labels=totals.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

def render_summary_metrics(df):
    """Shows total spending at a glance."""
    total = df["Amount"].sum() if not df.empty else 0
    st.metric("Total Spending", f"${total:,.2f}")