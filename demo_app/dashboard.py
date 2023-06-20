import streamlit as st
import pandas as pd
from data_analyzer import DataAnalyzer

class Dashboard:
    def __init__(self, data_analyzer: DataAnalyzer):
        self.data_analyzer = data_analyzer

    def generate(self):
        st.sidebar.subheader("Data Summary")
        summary = self.data_analyzer.get_summary()
        st.sidebar.write(summary)

        st.sidebar.subheader("Column Names")
        column_names = self.data_analyzer.get_column_names()
        st.sidebar.write(column_names)

        st.subheader("Data Visualization")
        st.write(self.data_analyzer.df)
