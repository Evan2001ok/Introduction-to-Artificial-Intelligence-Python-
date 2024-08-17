import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data into DataFrames
google_stock = pd.read_csv("./downloads/GOOG.csv", index_col="Date", usecols=["Date", "Adj Close"], parse_dates=True)
apple_stock = pd.read_csv("./downloads/AAPL.csv", index_col="Date", usecols=["Date", "Adj Close"], parse_dates=True)
amazon_stock = pd.read_csv("./downloads/AMZN.csv", index_col="Date", usecols=["Date", "Adj Close"], parse_dates=True)

# Rename the 'Adj Close' column for each stock
google_stock.rename(columns={'Adj Close': 'Google'}, inplace=True)
apple_stock.rename(columns={'Adj Close': 'Apple'}, inplace=True)
amazon_stock.rename(columns={'Adj Close': 'Amazon'}, inplace=True)

# Create a DataFrame with calendar dates
dates = pd.date_range('2000-01-01', '2016-12-31')
all_stocks = pd.DataFrame(index=dates)

# Join the individual stock DataFrames to the all_stocks DataFrame
all_stocks = all_stocks.join(google_stock).join(apple_stock).join(amazon_stock)

# Drop rows with any missing values
all_stocks.dropna(axis=0, inplace=True)

# Print the summary statisticsprint("Average stock price for each stock:\n", all_stocks.mean(), "\n")
print("Median stock price for each stock:\n", all_stocks.median(), "\n")
print("Standard deviation of the stock price for each stock:\n", all_stocks.std(), "\n")
print("Correlation between stocks:\n", all_stocks.corr(), "\n")

# Calculate the rolling mean for Google stock
rolling_mean = all_stocks["Google"].rolling(150).mean()

# Plot the Google stock data and its rolling mean
plt.figure(figsize=(10, 5))
plt.plot(all_stocks['Google'], label='Google Stock Price')
plt.plot(rolling_mean, label='150-Day Rolling Mean', color='orange')
plt.title('Google Stock Price with 150-Day Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.show()
