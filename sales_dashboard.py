import streamlit as st
import pandas as pd
import sqlite3

st.title("Sales Data Dashboard")

conn = sqlite3.connect("sales_project.db")

table = st.selectbox("Select Table to View:", ["sales"])

query = f"SELECT * FROM {table} LIMIT 20"
df = pd.read_sql_query(query, conn)

st.dataframe(df)

conn.close()
