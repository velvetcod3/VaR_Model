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


