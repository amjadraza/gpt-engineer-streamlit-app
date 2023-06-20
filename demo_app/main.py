import streamlit as st
import pandas as pd
from data_analyzer import DataAnalyzer
from dashboard import Dashboard

def upload_csv():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)

def main():
    st.title("CSV Data Analysis Dashboard")
    st.sidebar.title("Menu")

    # Upload CSV file
    df = upload_csv()
    if df is not None:
        # Analyze data and generate dashboard
        data_analyzer = DataAnalyzer(df)
        dashboard = Dashboard(data_analyzer)
        dashboard.generate()

if __name__ == "__main__":
    main()
