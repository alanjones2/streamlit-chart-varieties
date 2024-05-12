import streamlit as st
import pandas as pd
import altair as alt

cryptoW = pd.read_csv("crypto-23.csv")

cryptoL = cryptoW.melt(value_vars=['ETH','BTC'],var_name='Name',id_vars=['Month'])

# Display data
col1, col2 = st.columns(2)
col1.table(cryptoW)
col2.table(cryptoL)

fig = alt.Chart(cryptoL, 
                    width=800, 
                    title='Cryptocurrency closing prices'
                ).mark_line().encode(
                    x = 'Month:O',
                    y = 'value:Q',
                    color = 'Name:N')

st.altair_chart(fig)

fig = alt.Chart(cryptoL, 
                    width=800,
                    title='Cryptocurrency closing prices'
                ).mark_bar().encode(
                    x = 'Month:O',
                    y = 'value:Q',
                    color = 'Name:N',
                    xOffset = 'Name:N')

st.altair_chart(fig)

fig = alt.Chart(cryptoW, 
                width=800,
                title='Cryptocurrency closing prices'
                ).mark_point().encode(
                    x = 'BTC',
                    y = 'ETH')

trend = fig.transform_regression('BTC', 'ETH').mark_line()

st.altair_chart(fig + trend)

fig = alt.Chart(cryptoW, 
                width=800,
                title='Cryptocurrency closing prices'
                ).mark_point().encode(
                    x = alt.X('BTC',scale=alt.Scale(domain=[20000, 70000])),
                    y = 'ETH')

trend = fig.transform_regression('BTC', 'ETH').mark_line()

st.altair_chart(fig + trend)