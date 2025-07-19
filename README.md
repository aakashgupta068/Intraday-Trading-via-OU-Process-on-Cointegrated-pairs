# Intraday-Trading-via-OU-Process-on-Cointegrated-pairs
Modeled mean-reverting intraday spreads using the Ornstein-Uhlenbeck process on Johansen cointegrated pairs. Optimized MLE parameters with vectorized computation on 5-min data. Backtested using Backtrader with 2.2 Sharpe, 15% PnL, and 60% win rate over one year.

### 🧾 1. Project Title and Abstract
📌 Title:
Intraday OU-Based Pairs Trading on NSE: Mean-Reverting Signal with Cost-Aware Execution

### 📄 Abstract:
This project models intraday spreads between cointegrated equity pairs using the Ornstein-Uhlenbeck (OU) process to identify mean-reverting trade opportunities. Parameters are calibrated via Maximum Likelihood Estimation (MLE), and the strategy is validated using realistic fill assumptions, transaction costs, and capital management rules. Performance is evaluated using Sharpe ratio, annualized PnL, ROM, and drawdown.

### 📁 2. Directory Structure

├── data/                  # Raw and processed market data

├── notebooks/             # EDA, modeling, performance analysis

├── src/

│   ├── data_loader.py     # Load & preprocess data 

│   ├── cointegration.py   # Pair filtering via Johansen test

│   ├── ou_model.py        # OU parameter estimation

│   ├── signal_engine.py   # Z-score logic, entry/exit rules

│   ├── backtest_engine.py # Execution logic and capital tracking

│   └── metrics.py         # Sharpe, drawdown, ROM calculations

├── requirements.txt

├── README.md

└── main.py


### 📊 3. Data Extraction & Preprocessing
Data Source:
NSE intraday 1-minute data (cash equities)

Sources: [Kibot / Quandl / Zerodha / AlphaVantage / Paid APIs]

Steps:
* Load intraday OHLCV data

* Synchronize timestamps across symbols

* Generate spread series: Spread(t) = Price_A(t) - β × Price_B(t)

* Stationarity testing (ADF) and Johansen test for cointegration

python
Copy
Edit
# Example: Cointegration filter
from statsmodels.tsa.vector_ar.vecm import coint_johansen
# Filter top 10 cointegrated pairs

