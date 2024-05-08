import streamlit as st
import pandas as pd
import plotly.express as px

cryptoW = pd.read_csv("crypto-23.csv")

cryptoL = cryptoW.melt(value_vars=['ETH','BTC'],var_name='Name',id_vars=['Month'])

# Display data
col1, col2 = st.columns(2)
col1.table(cryptoW)
col2.table(cryptoL)

# Single line charts can be with wide data. Long data would need to be filtered
# ETH line chart
fig = px.line(cryptoW, x="Month", y="ETH", title='ETH values')
st.plotly_chart(fig)

# BTC line chart
fig = px.line(cryptoW, x="Month", y="BTC", title='BTC values')
st.plotly_chart(fig)

# Line chart with both ETH and BTC requires long data
fig = px.line(cryptoL, x="Month", y="value", color='Name', title='BTC and ETH values')
st.plotly_chart(fig)

# Grouped bar chart
fig = px.bar(cryptoL, x="Month", y="value", color="Name", barmode='group', title='BTC and ETH values')
st.plotly_chart(fig)

# Scatter plot with trend line
fig = px.scatter(cryptoW, x="ETH", y="BTC", trendline="ols", title='ETH values')
st.plotly_chart(fig)