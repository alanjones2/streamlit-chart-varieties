import streamlit as st
import pandas as pd
from bokeh.plotting import figure

cryptoW = pd.read_csv("crypto-23.csv")

cryptoL = cryptoW.melt(value_vars=['ETH','BTC'],var_name='Name',id_vars=['Month'])

# Display data
col1, col2 = st.columns(2)
col1.table(cryptoW)
col2.table(cryptoL)

# create a new plot with a title and axis labels
p = figure(title="Simple line example", 
          x_axis_label="Month", 
          y_axis_label="value")

# add a line renderer with legend and line thickness
p.line(cryptoW['Month'], 
      cryptoW['BTC'], 
      legend_label="BTC", 
      color = 'blue',
       line_width=2)
p.line(cryptoW['Month'], 
      cryptoW['ETH'], 
      legend_label="ETH", 
      color = "green",
       line_width=2)

st.bokeh_chart(p)

p = figure()


# Scatter
# add a circle renderer with x and y coordinates, size, color, and alpha
p.circle(cryptoW['BTC'], cryptoW['ETH'], size=8) 

st.bokeh_chart(p)

# Scatter plot with trend line
import numpy as np
# Calculate regression params
m,b = np.polyfit(cryptoW.BTC, cryptoW.ETH, 1)

# Add a trendline to the dataframe
cryptoW["trendline"] = [y for  y in  m*cryptoW.BTC + b]
st.table(cryptoW)

p.line(cryptoW['BTC'], 
      cryptoW['trendline'],  
      color = "green",
       line_width=2)

st.bokeh_chart(p)

# bar
from bokeh.transform import dodge
p = figure()

p.vbar(
    x=dodge("Month",0),
    top="BTC",
    width=0.4,
    source=cryptoW,
)
p.vbar(
    x=dodge("Month",-0.5),
    top="ETH",
    width=0.4,
    source=cryptoW,
    color='red'
)

st.bokeh_chart(p)