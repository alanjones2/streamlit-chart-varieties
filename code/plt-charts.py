import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

cryptoW = pd.read_csv("crypto-23.csv")

# Display data - no long data required
st.table(cryptoW)

# Line chart with both ETH and BTC still using wide data
fig, ax = plt.subplots()

ax.plot(cryptoW['Month'], cryptoW['BTC'])
ax.plot(cryptoW['Month'], cryptoW['ETH'])
plt.xlabel("Month")
plt.ylabel("Closing value (USD)")
plt.title("BTC/ETH performance")
plt.legend(['BTC','ETH'])
st.pyplot(fig)

# Grouped bar chart with both ETH and BTC still using wide data
fig, ax = plt.subplots()
width = 0.45
ax.bar(cryptoW['Month']-width/2, cryptoW['BTC'], width=width)
ax.bar(cryptoW['Month']+width/2, cryptoW['ETH'], width=width)
plt.xlabel("Month")
plt.ylabel("Closing value (USD)")
plt.title("BTC/ETH performance")
plt.legend(['BTC','ETH'])
st.pyplot(fig)

# Scatter plot with no trend line
fig, ax = plt.subplots()
ax.scatter(cryptoW['BTC'], cryptoW['ETH'])
plt.xlabel("BTC")
plt.ylabel("ETH")
plt.title("BTC/ETH correlation")
st.pyplot(fig)

# Scatter plot with trend line
import numpy as np
# Calculate regression params
m,b = np.polyfit(cryptoW.BTC, cryptoW.ETH, 1)

# Add a trendline to the dataframe
cryptoW["trendline"] = [y for  y in  m*cryptoW.BTC + b]
st.table(cryptoW)

ax.plot(cryptoW['BTC'], cryptoW['trendline'])

plt.xlabel("BTC")
plt.ylabel("ETH")
plt.title("BTC/ETH correlation")
st.pyplot(fig)