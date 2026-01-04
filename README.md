# 💰 ExpenseBuddy Pro

**ExpenseBuddy Pro** is a modern, interactive personal finance dashboard built with Python and Streamlit. It allows users to track daily expenses, manage budgets, and visualize spending habits through a "Fintrack-inspired" UI featuring custom KPI cards and interactive spline charts.

---

## 🚀 Features

* **Interactive Dashboard:** Custom CSS-styled "Metric Cards" with hover effects for high-level financial insights.
* **Visual Analytics:** * **Spline Area Chart:** Smooth trend lines for daily spending analysis.
    * **Donut Chart:** Categorical breakdown of expenses.
* **Data Persistence:** Automated CSV handling ensures your data is saved locally and never lost.
* **Easy Data Entry:** A streamlined sidebar form for adding transactions quickly.
* **Data Editor:** View and manage recent history via an interactive table.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (with Custom CSS Injection)
* **Backend:** Python
* **Data Handling:** Pandas
* **Visualization:** Plotly Express

---

## ⚙️ Installation & Setup

Follow these ordered steps to set up the project on your local machine.

### 1. Clone or Download the Repository
Navigate to the folder where you have the project files.

### 2. Create a Virtual Environment (Recommended)
This keeps your dependencies organized.

```bash
# Create the environment
python -m venv venv

## 📦 Project Deliverables

The following items are included in this project release:

### 1. Source Code
* **`main.py`**: The central controller script that launches the application.
* **`reports.py`**: The UI module handling custom CSS styling, KPI cards, and Plotly charts.
* **`menu.py`**: The input module managing sidebar forms and user interaction.
* **`file_manager.py`**: The backend module for CSV data persistence and retrieval.

### 2. Data & Configuration
* **`expenses.csv`**: The local storage file for persistent transaction history.
* **`requirements.txt`**: A comprehensive list of dependencies (`streamlit`, `pandas`, `plotly`) for easy environment setup.

### 3. Documentation
* **`README.md`**: Complete installation guide, usage instructions, and project overview.
* **Screenshots**: Visual evidence of the dashboard, data entry forms, and charts (located in the documentation).

### 4. Functional Application
* A fully interactive **Web Dashboard** accessible via localhost, featuring:
    * Real-time expense tracking.
    * Dynamic "Fintrack-style" visual analytics (Spline & Donut charts).
    * CRUD capabilities (Create/Read transactions).
