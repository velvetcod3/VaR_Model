import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Choice of 13 stock tickers selected

tickers = ['MSFT', '0700.HK', 'ABBV', 'MRK', 'NESN.SW', 'ULVR.L', 'DBK.DE', 'C', 'SHEL.L', '8058.T', 'CAT', 'MELI', 'JMIA']

# Tickers based on the following criteria filters 
max_beta = 1.5 
max_sector_weight = 0.35 
max_pe_ratio = 30
min_dividend_yield = 0.03 

market_caps = {}
filtered_stocks = []
sector_weights = {}

# Download market capitalization or historical price data for the tickers
for ticker in tickers:
    stock = yf.Ticker(ticker)
    
    # Fetch the market cap and store it in the market_caps dictionary
    market_data = stock.info
    market_caps[ticker] = market_data.get('marketCap', None)
    
# Display market caps
print(market_caps)

# Calculate total market capitalization
total_market_cap = sum(market_caps.values())

# Calculate the weights based on market capitalization
weights = {ticker: market_cap / total_market_cap for ticker, market_cap in market_caps.items()}

# Display portfolio weights
print(weights)
