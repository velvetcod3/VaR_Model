# Portfolio Construction and Risk Management Project 

## Project Description
This project constructs a portfolio based on stock selection criteria and applies risk management techniques, with a highlight on the Historical Value at Risk (VaR) and Sharpe Ratio, to evaluate performance.The aim is to immitate real world applications. To challenge myself to with a rebalancing strategy to replicate changing conditions. 


Future improvement to include

## Libaries
To run this project, you will need to install the following Python libraries:
- `yfinance` for downloading historical stock data
- `pandas` for data manipulation
- `numpy` for numerical calculations
- `matplotlib` for data visualization
- `statsmodels` for time series analysis (if using the VAR model)



 ## Performance Metrics

1. **Sharpe Ratio**: Measures the portfolio’s risk-adjusted return.
2. **Volatility**: Annualized standard deviation of returns, indicating risk.
3. **Maximum Drawdown**: The largest peak-to-trough decline in the portfolio's value during the period.
4. **Value at Risk (VaR)**: Estimates the potential loss for the portfolio over a given time period and confidence level.
5. **Cumulative Returns**: Shows how the portfolio's total value grows over time.
   
### Completed:
- **Evalauting Tickers**: selected based on the following criteria (Beta yield, Dividened yield, Maximum sector Weight).
- Historical gathering of the data from the last 5 years. 
  



### In Progress:
- 🔄 **Beta Calculation and Market Cap Adjustment**: Developing methods to integrate sector weights and market caps effectively into portfolio management.
- 🔄 **VaR Calculation**: Currently working on historical and parametric VaR models to quantify portfolio risk.

### To Do:
- ⬜ **User Interface Development**: Create a basic interface for users to interact with the portfolio, choose assets, and view VaR.
- ⬜ **Data Visualization**: Develop visualizations to help users better understand risk metrics and portfolio composition.
- ⬜ **Testing and Validation**: Conduct tests to validate the accuracy of the VaR calculations.

## Installation
To use the current version of this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/stock-portfolio-VaR.git
    ```
2. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```
   
## How to Use the Current Code
### Usage
Currently, the available script helps collect historical data and construct a basic stock portfolio. To run the current script, use:
```bash
python main.py


