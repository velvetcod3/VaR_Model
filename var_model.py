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
        
        # Apply selection criteria 
        if beta <= max_beta and pe_ratio <= max_pe_ratio:
            print(f"{ticker} passed the criteria")

            try:
                # Download 5 years of historical data for this stock
                stock_data = yf.download(ticker, period='5y')
                historical_data[ticker] = stock_data['Adj Close']

                # Add a 2-second delay to avoid rate-limiting issues
                time.sleep(2)  # Delay of 2 seconds after each request


            except Exception as e:
                # Handle any exceptions raised during the download of stock data
                print(f"Error downloading historical data for {ticker}: {e}")
         
    
#skipping the JUMIA (due to negative P/E) and MELI (missing data) and ABBV (P/E Ratio too high)


    except Exception as e:
        # Handle any exceptions raised in the try block
     print(f"Error processing {ticker}: {e}")

# Check the final combined historical data
print(historical_data)


# Print the skipped stocks
print("\nSkipped Stocks:")
print(skipped_stocks)

total_market_cap = sum([market_data['marketCap'] for market_data in filtered_stocks])
weights = [stock['marketCap'] / total_market_cap for stock in filtered_stocks]

# --- Portfolio Returns Calculation ---

# Calculate daily returns for each stock
stock_returns = historical_data.pct_change().dropna()

# Calculate total market cap for weighted returns
total_market_cap = sum([stock['marketCap'] for stock in filtered_stocks])

# Calculate weights based on market cap
weights = np.array([stock['marketCap'] / total_market_cap for stock in filtered_stocks])
