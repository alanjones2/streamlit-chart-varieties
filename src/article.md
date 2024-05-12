# Streamlit Supports 5 Important Data Visualization Libraries - Which to Choose?

## We code examples using Altair, Bokeh, Plotly, Pandas Plot and Matplotlib, to illustrate the pros and cons of each one

Imagine your organisation has decided to use Streamlit as its primary platform for showcasing data visualization applications and, to ensure a consistent look, it wants to adopt a single graphing library to be used across all applications. Your job is to investigate which is most appropriate.

You are spoiled for choice! There are 5 libraries you can use for coding your data visualizations: Altair, Bokeh, Plotly, Pyplot (Matplotlib) and Vega Lite. And Streamlit provides some native charts, as well.

Let's take a look at each one and code up some commonly used charts. 

The data that we will use is a set of price data for a pair of cryptocurrencies and from that data we will create:

- A line chart showing the change in closing prices over a year for both currencies.

- A grouped bar chart showing the same data, again, for both currencies.

- A scatter chart with a trendline showing the correlation between the change in value of the two currencies.

The charts will look similar to the ones in the image below.

![](../images/rowcharts.png)

But let's do a quick review of the options so we can eliminate any obvious non-starters.

### Built-in charts

The first thing to look at is the set of built-in functions that Streamlit provides. They will draw simple line charts, bar charts and scatter plots. And, as the documentation states, these are simply wrappers around the Altair equivalents. The documentation also suggests that if these simple charts don't work for you, you should use the Altair charts, instead.

A quick look at the documentation will confirm that these charts cannot produce any of the three charts in this experiment.

### Vega-Lite

Vega-Lite is a powerful graphing language which requires you to create a specification for the chart that you want to draw in a specific JSON format. This is a rather arduous and error-prone task. If you already have Vega-Lite specifications to hand then this is clearly the function you want to use but to create them from scratch it has to be better to use the Altair library which is a Python-friendly way of producing the same thing.







- Streamlit's `st.pyplot()`function is a way of displaying Matplotlib figures but, of course, there are other plotting libraries that are built on Matplotlib: Seaborn and Pandas Plots, for example. To show how we can use these we will include a version of the graphs created with Pandas Plots as well as directly in Matplotlib.

So, we will create the three graphs in each of Altair, Bokeh, Matplotlib, Pandas Plots and Plotly.
