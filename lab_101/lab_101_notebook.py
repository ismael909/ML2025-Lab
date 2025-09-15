#!/usr/bin/env python
# coding: utf-8

# <img align="center" style="max-width: 900px; height: auto" src="../assets/banner.png">

# <img align="right" style="max-width: 200px; height: auto" src="../assets/hsg_logo.png">
# 
# ###  Lab 101 - Introduction to Python and Jupyter
# 
# 7,854,1.00 Machine Learning, University of St.Gallen (HSG)

# The lab environment of the **7,854,1.00 Machine Learning** course is powered by Jupyter Notebooks (https://jupyter.org), which allows one to perform a great deal of data analysis and statistical validation. In this first lab, we want to touch on the basic concepts and techniques of such notebooks. Furthermore, its capabilities will be demonstrated based on a few simple and introductory examples.

# ### Lab Objectives:

# After today's lab, you should be able to:
#     
# > 1. Understand the general workflow, structure, and functionality of **Jupyter** notebooks.
# > 2. Import and apply python data science libraries such as `NumPy` and `Pandas`.
# > 3. Understand how the **Python** programming language can be utilized to manipulate and analyze financial data.
# > 4. Download arbitrary stock market and financial data using the `Pandas` `DataReader` API.
# > 5. Use the `Matplotlib` library to visualize data as well as analytical results.

# Note: The content of this first lab is inspired by the Quantopian lecture series ( https://www.quantopian.com ). If you are interested to learn more about financial data science and/or algorithmic trading their lectures are a great resource to get you started.

# ### 1. Jupyter Notebook Introduction

# #### Code Cells vs. Text Cells

# As you can see, each cell can be either code or text. To select between them, choose from the `Cell Type` dropdown menu on the top left.

# Hello World!

# In[2]:


1 + 5


# #### Executing a Command

# A code cell will be evaluated when you press **'Run'**, or when you press the shortcut, shift-enter. Evaluating a cell evaluates each line of code in sequence, and prints the results of the last line below the cell.

# In[ ]:


40 + 2


# Sometimes there is no result to be printed, as is the case with the following assignment:

# In[ ]:


X = 2


# In[ ]:


X


# Remember that only the result from the last line is printed.

# In[ ]:


2 + 2
3 + 3


# However, you can print whichever lines you want using the print statement.

# In[ ]:


print(2 + 2)
3 + 3


# #### Comments
# 
# The `#` character has a special meaning in Python. Whenever it appears, all following characters on the same line are considered as comments and are ignored. You can use comments to explain what certain parts of your code do.

# In[ ]:


# this is a comment


# In[ ]:


print(1) # comments can be on the same line as code


# #### Knowing When a Cell is Running

# While a cell is running, a **[*]** will be displayed on the left of the respective cell. When a cell has yet to be executed, **[ ]** will be displayed. When it has been run, a number will display indicating the order in which it was run during the execution of the notebook **[5]**. Try on this cell and note what is happening:

# In[ ]:


# take some time to run something
c = 0
for i in range(10000000):
    c = c + i
c


# ### 2. Importing Python Libraries

# The vast majority of the time, we will use functions from pre-built libraries, such as:

# In[ ]:


# importing the python sys library
import sys


# You can check your Python version at the command line by running:

# In[ ]:


# determine the python system version
sys.version


# You can't import every library into the lab environment due to security issues. However, you can import most of the common scientific ones. Here we import the libraries `NumPy` (https://www.numpy.org) and `Pandas` (https://pandas.pydata.org), two of the most common and useful libraries in data science. We recommend copying this import statement for every new notebook that you will create.

# In[ ]:


# import the number and Pandas data science libraries
import numpy
import pandas


# Let's now use the `NumPy` library to calculate the mean of a list of numbers:

# In[ ]:


numpy.mean([1, 2, 3, 4])


# Notice that you can rename libraries to whatever you want after importing. The `as` statement allows this. Here we use `np` and `pd` as aliases for both the pre-built `NumPy` and `Pandas` libraries. This is very common aliasing and will be found in most code snippets around the web. The idea behind this is to allow you to type fewer characters when you are frequently accessing these libraries.

# In[ ]:


# importing the NumPy and Pandas data science libraries using aliases
import numpy as np
import pandas as pd


# Let's now use the `NumPy` library to calculate the mean of a list of numbers:

# In[ ]:


np.mean([1, 2, 3, 4])


# ### 3. Code Completion and Documentation

# #### Autocomplete Code

# Pressing tab will give you a list of Jupyter's best guesses for what you might want to type next. This is incredibly valuable and will save you a lot of time. If there is only one possible option for what you could type next, Jupyter will fill that in for you. Try pressing tab very frequently; it will seldom fill in anything you don't want as if there is ambiguity a list will be shown. This is a great way to see what functions are available in a library.
# 
# Try placing your cursor after the `.` and press the `tab` key on your keyboard (or `shift` + `tab` when it doesn't work).

# In[ ]:


np.random.gamma


# #### Documentation Help

# Placing a question mark after a function and executing that line of code will give you the documentation Jupyter has for that function. It's often best to do this in a new cell, as you avoid re-executing other code and running into bugs.

# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.random.normal')


# ### 4. Plotting Data

# #### Random Data Sampling

# Let's' sample some random data using a function from `NumPy`.

# In[ ]:


# sample 100 points with a mean of 0 and an std of 1. This is a standard normal distribution.
x = np.random.normal(0, 1, 100)


# In[ ]:


x


# #### Data Plotting

# Python's `Matplotlib` library (https://matplotlib.org) is a very flexible library and has a lot of handy, built-in defaults that will help you out tremendously.
# 
# As such, you don’t need much to get started: you need to make the necessary imports, prepare some data, and you can start plotting with the help of the `plot()` function. Let's have a look.

# Let's import Matplotlib by running the following statements:

# In[ ]:


# importing the matplotlib plotting library
import matplotlib.pyplot as plt


# Note that we imported the `pyplot` module of the `Matplotlib` library under the alias `plt`.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')


# We can now use the plotting functionality provided by Matplotlib as follows:

# In[ ]:


plt.plot(x)


# Let's apply some variations as well as the axis legends to our plot:

# In[ ]:


plt.plot(x, linewidth=3, linestyle="--")

# set label and title details
plt.xlabel('sample', weight='normal', fontsize=8)
plt.ylabel('value', weight='normal', fontsize=8)


# #### Remove Line Output

# You might have noticed a similar annoying line of the form: `[<matplotlib.lines.Line2D at 0x10a4cce90>]` before the created plot. If you wish to get rid of this output, end the plot statement using a semicolon `;`:

# In[ ]:


plt.plot(x);


# #### Adding Axis Labels

# No self-respecting quantitative analyst leaves a graph without labeled axes. Here are some commands to help with that.

# In[ ]:


# sample 100 points twice with a mean of 0 and an std of 1 from a standard normal distribution.
x1 = np.random.normal(0, 1, 100)
x2 = np.random.normal(0, 1, 100)


# In[ ]:


# plot both sample results
plt.plot(x1);
plt.plot(x2);

# add x-axis and y-axis label
plt.xlabel('Time')
plt.ylabel('Returns')

# add plot legend
plt.legend(['X1', 'X2'])

# add plot title
plt.title('Sample Returns X1 and X2');


# ### 5. Generating Statistics

# Let's use `NumPy` to take some simple statistics like the mean of the generated samples:

# In[ ]:


np.mean(x1)


# As well as the corresponding standard deviation of the generated samples:

# In[ ]:


np.std(x1)


# ### 6. Collect and Plot Real Pricing Data

# One of the first steps to any data science project is usually to import your data. Randomly sampled data can be great for testing ideas, but let's now import some real financial market data.
# 
# As part of the `Labs` section of the **Machine Learning** Git repository, you will find a "Comma Separated Value (CSV)" file named `sample_google_data_daily.csv`. The file contains the daily stock market data of the **Alphabet (Google) Inc.** stock within the time frame `31-12-2015` till `31-12-2017`. In a next step, we define a variable that stores the URL under which the file is located:

# In[ ]:


file_url = 'https://raw.githubusercontent.com/HSG-AIML-Teaching/ML2025-Lab/main/lab_101/sample_google_data_daily.csv'


# Once we have specified the file URL we are able to import the file into Python using the `read_csv()` function of the `Pandas` library by running the following statement:

# In[ ]:


alphabet_data = pd.read_csv(file_url, sep=';')


# The retrieved data is a so-called `Pandas` `DataFrame`. You can see the datetime index and the columns with different pricing data. Let's inspect the top 5 rows of the imported data using the `head()` function of the `Pandas` library:

# In[ ]:


alphabet_data.head(5)


# Looks good, right?

# It's great to import data that was already collected and stored accordingly. Unfortunately, in real data science projects, we are often challenged to retrieve the data from a variety of sources, e.g., the web. But where to get financial data of good quality? A great source for retrieving such data can be found in the `Pandas` `Datareader`package.
# 
# Although the **Google Colab** environment comes with a lot of pre-installed libraries, sometimes a needed library might not be available. Therefore, you may want to install libraries directly within an individual notebook. Please note, libraries installed from the notebook apply only to the current server session. Library installations aren't persistend once the server is shut down.

# In general, libraries in Python can be installed using the shell **pip** command within code cells. Any command that works at the command-line can be used in Jupyter Notebbos by prefixing it with the `!` character. Let's give it a try and install the `pandas_datareader` python library.

# In[ ]:


get_ipython().system('pip3 install yfinance --ignore-installed')


# Let's import the `DataReader` as well as the `DateTime`library to retreive some financial data:

# In[ ]:


import datetime as dt
import yfinance as yf


# Specify both the `start` and `end` date of the data download:

# In[ ]:


start_date = dt.datetime(2024, 1, 1)
end_date = dt.datetime(2024, 12, 31)


# Download the daily **Tesla Inc.** (ticker symbol: TSLA) stock data using the `yfinance` library, which gives us  `Pandas` `dataframe`:

# In[ ]:


# download tesla market data
tesla_data = yf.download('TSLA', start=start_date, end=end_date)


# Let's inspect the top 5 rows of the imported data using the `head()` function of the `Pandas` library:
# 
# > Add blockquote
# 
# 

# In[ ]:


tesla_data.head(5)


# To obtain an initial understanding of the date retrieved, let us have a look at some basic data statistics:

# In[ ]:


tesla_data.describe()


# Ok, at first glance, the data looks fine. Let's, therefore, save it to your local directory using the `to_excel()` function of the `Pandas` library:

# In[ ]:


tesla_data.to_excel('sample_tesla_data_daily.xlsx', sheet_name='TSLA_data')


# \To get a specific column of a `Pandas` dataframe, we can column-slice it to get the closing price from data like this:

# In[ ]:


tesla_closing = tesla_data['Close']


# Let's inspect the **top 5** rows of the sliced data:

# In[ ]:


tesla_closing.head(5)


# Ok great, we got two columns (1) the index 'Date' of the DataFrame as well as (2) the data column 'Adj. Close' price that we asked for.

# Let's now plot the date vs. the adjusted closing prices. But before doing so, we need to be able to disentangle the index from the data. This can be accomplished by the `.index` function that will return the index of a given DataFrame as well as the `.values` function that will return the actual data (excl. the index) of a given DataFrame. We will use both commands to specify the X and Y coordinates of the plot:

# In[ ]:


# plot both sample results
plt.plot(tesla_closing.index, tesla_closing.values)

# tesla_closing.plot()

# add x-axis and y-axis label
plt.xlabel('Time')
plt.ylabel('Closing Price')

# add plot title
plt.title('Tesla Inc. Daily Adjusted Closing Price');


# In[ ]:


np.mean(tesla_closing.values)


# In[ ]:


np.std(tesla_closing.values)


# ### 7. Obtaining Returns from Prices

# When analyzing stock market data, we are often also interested in the return $R_t$ of a financial instrument over a certain time frame:

# $$R_t=\frac{V_{f}-V_{i}}{V_{i}}$$

# where:
# 
# - $V_{f}$ denotes the financial instruments final value, including dividends and interest
# - $V_{i}$ denotes the financial instruments initial value
# 
# The `Pandas` data science library provides us with a variety of functions that come quite "handy" when analyzing such data. To determine the daily return $r_t$ we may, for example, utilize Pandas `pct_change` function:

# In[ ]:


tesla_returns = tesla_closing.pct_change()


# Let's inspect the calculated returns:

# In[ ]:


tesla_returns.head(5)


# Notice, how we drop the first element after doing this, as it will be `NaN`.

# In[ ]:


tesla_returns = tesla_returns[1:]


# And inspect the returns data again:

# In[ ]:


tesla_returns.head(5)


# Let's now plot the distribution of daily returns as a histogram:

# In[ ]:


# plot histogram of returns
plt.hist(tesla_returns, bins=20)

# add x-axis and y-axis label
plt.xlabel('Return')
plt.ylabel('Frequency')

# add plot title
plt.title('Tesla Inc. Adjusted Daily Returns');


# Let's again get statistics on the real daily return data:

# In[ ]:


np.mean(tesla_returns)


# In[ ]:


np.std(tesla_returns)


# Let's generate data out of a normal distribution using the statistics we estimated from the daily returns of the Tesla stock. We'll see that we have good reason to suspect the Tesla returns may not be normally distributed, as the resulting normal distribution looks far different.

# In[ ]:


# plot histogram of randomly sampled returns
plt.hist(np.random.normal(np.mean(tesla_returns), np.std(tesla_returns), 10000), bins=20)

# add x-axis and y-axis label
plt.xlabel('Return')
plt.ylabel('Frequency')

# add plot title
plt.title('Tesla Inc. Adjusted Daily Returns (Normal)');


# ### 8. Generating a Moving Average

# When analyzing stock market data, we are often also interested in calculating so-called "rolling statistics", e.g., a 90- or 200-day moving average. Again the `Pandas` library is offering some great functions that allow us to generate such rolling statistics. Here's an example. Notice how there's no moving average for the first 30 days, as we don't have 90 days before we can determine the first value:

# In[ ]:


# determine the rolling average of the last 90 days
tesla_moving_average = tesla_closing.rolling(window=90, center=False).mean()


# Let's plot the obtained moving averages.

# In[ ]:


# plot quarterly returns
plt.plot(tesla_closing.index, tesla_closing.values)

# plot moving averages quarterly returns
plt.plot(tesla_moving_average.index, tesla_moving_average.values)

# add x-axis and y-axis label
plt.xlabel('Return')
plt.ylabel('Price')

# add plot legend
plt.legend(['Return', '90-day MAVG']);

# add plot title
plt.title('Tesla Inc. Returns vs. Moving Average Returns');


# ### Lab Assignments:

# You may want to try the following exercises after the lab:

# **1. Download data using the library `yfinance`.**
# 
# > Download the daily closing prices of the three following stocks: Netflix, Facebook, and Microsoft. Download the daily stock closing prices starting from 2014-01-01 until today as a `Pandas` DataFrame.

# In[ ]:


# ***************************************************
# INSERT YOUR CODE HERE
# ***************************************************


# Throughout the course, we will visualize and analyze plenty of data. The following exercises should provide you a first intuition on how this can be achieved using Python's `Pandas` and `Matplotlib` library:
# 
# **2. Visualise data using the `Matplotlib` library, `plt.plot(...)` and `plt.hist(...)`.**
# 
# > Visualize the downloaded data by plotting the daily adjusted closing prices of the three stocks over time (1) into a single plot for each stock as well as (2) into a single plot containing the closing prices of all three stocks combined.

# In[ ]:


# ***************************************************
# INSERT YOUR CODE HERE
# ***************************************************


# **3. Save data using the `Pandas` library.**
# 
# > Research the `Panda's` data science library on how to save a `Pandas` `DataFrame` to a local directory. Save the raw daily closing prices and corresponding date of all three stocks in a comma-separated value (CSV) format to your local directory. Save the CSV file using the semicolon `';'` separator.

# In[ ]:


# ***************************************************
# INSERT YOUR CODE HERE
# ***************************************************


# **4. Analyze data using the `Pandas` library, `data.rolling(..., window=...)`.**
# 
# > For each stock, calculate the rolling moving averages of the daily closing prices using a time window of 30 and 90 days. For each stock, plot the daily closing price as well as the 30 and 90 days moving average into a single plot.

# In[ ]:


# ***************************************************
# INSERT YOUR CODE HERE
# ***************************************************


# ### Lab Summary:

# In this initial lab, a step by step introduction into some basic concepts of analyzing financial data using Jupyter notebooks are presented. The code and exercises presented in this lab may serve you as a starting point for more complex and tailored analytics.

# You may want to execute the content of your lab outside of the Jupyter notebook environment, e.g., on a compute node or a server. The cell below converts the lab notebook into a standalone and executable python script.

# In[ ]:


get_ipython().system('jupyter nbconvert --to script lab_101_notebook.ipynb')

