import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import time
import random

# Choice of 13 stock tickers selected, excluding JUMIA and MELI and ABBV

tickers = ['MSFT', '0700.HK', 'MRK', 'NESN.SW', 'ULVR.L', 'DBK.DE', 'C', 'SHEL.L', '8058.T', 'CAT',]

# Tickers based on the following criteria filters 
max_beta = 1.5 
max_sector_weight = 0.35 
max_pe_ratio = 40


market_caps = {}
filtered_stocks = []
sector_weights = {}
historical_data = pd.DataFrame()


# List to store skipped stocks
skipped_stocks = []


# Download stock data with error handling
for ticker in tickers:
    stock = yf.Ticker(ticker)

# Add a 2-second delay to avoid rate-limiting issues
    time.sleep(5)

    try:
        # Fetch stock info and handle missing or problematic data
        market_data = stock.info
        market_cap = market_data.get('marketCap', None)
        beta = market_data.get('beta', None)
        pe_ratio = market_data.get('trailingPE', None)
        sector = market_data.get('sector', 'Unknown')
        

        # Error handling: Ensure data is present before applying criteria
        if market_cap is None or beta is None or pe_ratio is None:
            print(f"Missing data for {ticker}, skipping...")
            continue  # Skip this stock if any required data is missing
        

    except Exception as e:
        print(f"Error fetching market data for {ticker}: {e}")
        skipped_stocks.append(ticker)
        continue  # Skip this stock
    


        # Applying selection criteria 
    try:
        if beta <= max_beta and pe_ratio <= max_pe_ratio:
            print(f"{ticker} passed the criteria")
            filtered_stocks.append({'ticker': ticker, 'marketCap': market_cap})
        else:
            print(f"{ticker} did not pass the criteria")
            skipped_stocks.append(ticker)
            continue

    except Exception as e:
        print(f"Error applying selection criteria for {ticker}: {e}")
        skipped_stocks.append(ticker)
        continue

#skipping the JUMIA (due to negative P/E) and MELI (missing data) and ABBV (P/E Ratio too high)


# Download 5 years of historical data for this stock

    try:
        stock_data = yf.download(ticker, period='5y')
        historical_data[ticker] = stock_data['Adj Close']

        # Add a 5-second delay to avoid rate-limiting issues
        time.sleep(5)  # Delay of 5 seconds after each request


    except Exception as e:
                # Handle any exceptions raised during the download of stock data
        print(f"Error downloading historical data for {ticker}: {e}")
        skipped_stocks.append(ticker)

          
    
# Check the final combined historical data
print(historical_data)


# Print the skipped stocks
print("\nSkipped Stocks:")
print(skipped_stocks)

# Calculate total market cap and weights
total_market_cap = sum([stock['marketCap'] for stock in filtered_stocks])
weights = [stock['marketCap'] / total_market_cap for stock in filtered_stocks]


# Define initial_weights here
initial_weights = weights.copy()  # Make a copy to preserve original weights

# Convert historical data to daily returns
daily_returns = historical_data.pct_change(fill_method=None).dropna()

# Calculate portfolio daily returns using the weights
portfolio_daily_returns = daily_returns.dot(weights)

# Calculate the portfolio variance
portfolio_variance = np.dot(weights, np.dot(daily_returns.cov(), weights))

# Print out results
print("\nPortfolio Weights:")
print(weights)

print("\nPortfolio Daily Returns:")
print(portfolio_daily_returns)

print("\nPortfolio Variance:")
print(portfolio_variance)

#Find the stock with more than 60% weight
threshold_weight = 0.5  # 60% threshold
max_weight = 0.2  # Cap any weight to a maximum of 20%

# Zip the weights with their corresponding tickers for easy identification
weights_with_stocks = list(zip([stock['ticker'] for stock in filtered_stocks], initial_weights))

# Add a 2-second delay to avoid rate-limiting issues
time.sleep(5)

# Identify the stock with weight > 60%
for ticker, weight in weights_with_stocks:
    if weight > threshold_weight:
        print(f"Stock '{ticker}' has more than 60% weight ({weight * 100:.2f}%). Capping at 20%.")
        excess_weight = weight - max_weight
        break

    # Add a 2-second delay to avoid rate-limiting issues
    time.sleep(5)

    
# Redistribute the excess weight among other stocks proportionally
total_remaining_weight = 1 - max_weight
adjusted_weights = []
for ticker, weight in weights_with_stocks:
    if weight > threshold_weight:
        # Cap the weight of the stock that exceeds 60%
        adjusted_weights.append(max_weight)
    else:
        # Redistribute the remaining weights proportionally
        adjusted_weights.append(weight + (weight / (1 - weight) * excess_weight))

# Print the updated weights
print("Updated Weights:", adjusted_weights)
