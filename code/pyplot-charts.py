import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib

matplotlib.style.use('seaborn-v0_8-white')
#plt.style.available

matplotlib.rcParams['font.size'] = 8

cryptoW = pd.read_csv("crypto-23.csv")

# Display data - no long data required
st.table(cryptoW)

# ETH line chart
fig, ax = plt.subplots()
cryptoW.plot(y='ETH', x='Month', title='ETH values', ax=ax)
st.pyplot(fig)

# BTC line chart
fig, ax = plt.subplots()
cryptoW.plot(y='BTC', x='Month', title='BTC values', ax=ax)
st.pyplot(fig)

# Line chart with both ETH and BTC still using wide data
fig, ax = plt.subplots()
cryptoW.plot(y=['BTC','ETH'], x='Month', title='BTC and ETH values', ax=ax)
st.pyplot(fig)

# Grouped bar chart with both ETH and BTC still using wide data
fig, ax = plt.subplots()
cryptoW.plot.bar(y=['BTC','ETH'], x='Month', 
                 title='BTC and ETH values', ax=ax)
st.pyplot(fig)

# Scatter plot with no trend line
fig, ax = plt.subplots()
ax = cryptoW.plot.scatter(y='ETH', x='BTC', 
                          title='BTC and ETH values', ax=ax)
st.pyplot(fig)

# Scatter plot with trend line
import numpy as np

# Calculate regression params
m,b = np.polyfit(cryptoW.BTC, cryptoW.ETH, 1)

# Add a trendline to the dataframe
cryptoW["trendline"] = [y for  y in  m*cryptoW.BTC + b]
st.table(cryptoW)

# Add the line over the existing scatter plot
cryptoW.plot(x = 'BTC', y = 'trendline', ax=ax)
st.pyplot(fig)
