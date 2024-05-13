import streamlit as st
import pandas as pd
from bokeh.plotting import figure

cryptoW = pd.read_csv("crypto-23.csv")

# Display data
st.table(cryptoW)

# create a new plot with a title and axis labels
p = figure(title="Line chart ETH and BTC prices", 
          x_axis_label="Month", 
          y_axis_label="Value (USD)",
          width=800)

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
p.legend.location = "top_left"

st.bokeh_chart(p)

# Scatter
# add a circle renderer with x and y coordinates, size, color, and alpha
p = figure(title="Scatter chart BTC/ETH", 
          x_axis_label="BTC", 
          y_axis_label="ETH",
          width=800)

p.circle(cryptoW['BTC'], cryptoW['ETH'], size=8) 

#st.bokeh_chart(p)

# Add trend line to scatter plot
import numpy as np
# Calculate regression params
m,b = np.polyfit(cryptoW.BTC, cryptoW.ETH, 1)

# Add a trendline to the dataframe
cryptoW["trendline"] = [y for  y in  m*cryptoW.BTC + b]
#st.table(cryptoW)

p.line(cryptoW['BTC'], 
      cryptoW['trendline'],  
      color = "green",
       line_width=2)

st.bokeh_chart(p)

# Grouped bar chart
from bokeh.transform import dodge
p = figure(title="Grouped bar", 
          x_axis_label="Month", 
          y_axis_label="Value (USD)",
          width=800)
width = 0.4

p.vbar(
    x=dodge("Month",width/2), 
    legend_label="BTC",
    top="BTC",
    width=width,
    source=cryptoW,
    color='blue'
)
p.vbar(
    x=dodge("Month",-width/2), 
    legend_label="ETH",
    top="ETH",
    width=width,
    source=cryptoW,
    color='green'
)
p.legend.location = "top_left"
st.bokeh_chart(p)