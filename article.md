# Streamlit Supports 5 Important Data Visualization Libraries - Which to Choose?

## We code examples using Altair, Bokeh, Plotly, Pandas Plot and Matplotlib, to illustrate the pros and cons of each one

Imagine your organisation has decided to use Streamlit as its primary platform for showcasing data visualization applications and, to ensure a consistent look, it wants to adopt a single graphing library to be used across all applications. And, let's say, your job is to investigate which is most appropriate.

You are spoiled for choice! There are 5 libraries you can use for coding your data visualizations: Altair, Bokeh, Plotly, Pyplot (Matplotlib) and Vega Lite. And Streamlit provides some native charts, as well.

Let's take a look at each one and code up some commonly used charts. 

The data that we will use is a set of price data for a pair of cryptocurrencies and from that data we will create:

- A line chart showing the change in closing prices over a year for both currencies.

- A grouped bar chart showing the same data, again, for both currencies.

- A scatter chart with a trendline showing the correlation between the change in value of the two currencies.

The charts will look similar to the ones in the image below.

![](../images/rowcharts.png)

### The data

The dataset we will use is a simple three-column dataframe. It tracks the closing prices of two cryptocurrencies over a 12-month period. It is not important for the exercise but the currencies are Ethereum and Bitcoin and the period is the previous 12 months. (The data are a matter of public record and are available from several sources. I retrieved them from [Yahoo Finance]([Crypto Real Time Prices &amp; Latest News - Yahoo Finance](https://finance.yahoo.com/crypto/)).)

### The options

First, let's do a quick review of the options so we can eliminate any obvious non-starters.

__Built-in charts__

The first thing to look at is the set of built-in functions that Streamlit provides. They will draw simple line charts, bar charts and scatter plots. And, as the documentation states, these are simply wrappers around Altair equivalents. The documentation also suggests that if these simple charts don't work for you, you should use the Altair charts, instead.

A quick look at the documentation will confirm that these charts cannot produce any of the three charts in this experiment. So we won't explore these any further.

__Vega-Lite__

Vega-Lite is a powerful graphing language that specifies charts in a JSON format. Writing a Vege-Lite specification can be an arduous and error-prone task, and that is why Altair was developed. Altair is a Python library that outputs Vega-Lite specs, so If you already have Vega-Lite specifications to hand then the Vega-Lite library is the obvious one to use. But to create a chart from scratch it has to be better to use the Altair library which is a Python-friendly way of producing the same thing.

__The rest__

The remaining libraries are all powerful and Python-friendly ways of producing sophisticated charts and we will explore them further.  But we'' look at one of the libraries in two ways.'

Streamlit's `st.pyplot()`function is a way of displaying Matplotlib figures but, of course, there are other plotting libraries that are built on Matplotlib: Seaborn and Pandas Plots, for example. To show how we can use these we will include a version of the graphs created with Pandas Plots in addition to those created directly in Matplotlib.

So, we will create the three graphs in each of Altair, Bokeh, Matplotlib, Pandas Plots and Plotly.

### Altair



### Bokeh



### Matplotlib



### Pandas Plots



### Plotly



### So, where does that leave us


