import streamlit as st
import file_manager as fm
import menu
import reports

# 1. Page Configuration
st.set_page_config(page_title="ExpenseBuddy Pro", page_icon="💰")

# 2. Draw Sidebar (Input area)
menu.draw_sidebar()

# 3. Load Data & Show Dashboard (Output area)
st.title("📊 My Personal Finance Dashboard")
df = fm.load_expenses()

if not df.empty:
    reports.render_summary_metrics(df)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Transaction History")
        st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)
    with col2:
        st.subheader("By Category")
        reports.render_category_pie(df)
else:
    st.info("No data yet! Add an expense in the sidebar to get started.")