import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
                   
cryptoW = pd.read_csv("crypto-23.csv")

cryptoL = cryptoW.melt(value_vars=['ETH','BTC'],var_name='Name',id_vars=['Month'])

# Single line charts can be with wide data. Long data would need to be filtered
# ETH line chart

# Line chart with both ETH and BTC requires long data
fig1 = px.line(cryptoL, x="Month", y="value", 
               color='Name', 
               title='BTC and ETH values')
fig1.update_traces(line={'width': 8})
st.plotly_chart(fig1)

# Grouped bar chart
fig2 = px.bar(cryptoL, x="Month", y="value", color="Name", barmode='group', title='BTC and ETH values')

st.plotly_chart(fig2)

# Scatter plot with trend line
fig3 = px.scatter(cryptoW, x="ETH", y="BTC",
                  trendline="ols", title='ETH values')
fig3.update_traces(line={'width': 8, 'color':'lightblue'})
fig3.update_traces(marker_size=20)
fig3.update_traces(marker_color='blue')

st.plotly_chart(fig3)

cols = st.columns(3)
cols[0].plotly_chart(fig1)
cols[1].plotly_chart(fig2)
cols[2].plotly_chart(fig3)