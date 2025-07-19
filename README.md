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

├── main.py

├── src/

│   ├── data_loader.py     # Load & preprocess data 

│   ├── cointegration.py   # Pair filtering via Johansen test

│   ├── ou_model.py        # OU parameter estimation

│   ├── signal_engine.py   # Z-score logic, entry/exit rules

│   ├── backtest_engine.py # Execution logic and capital tracking

│   └── metrics.py         # Sharpe, drawdown, ROM calculations

├── requirements.txt

└── README.md


### 📊 3. Data Extraction & Preprocessing
Data Source:
NSE intraday 1-minute data (cash equities)

Sources: [Kibot / Quandl / Zerodha / AlphaVantage / Paid APIs]

Steps:
* Load intraday OHLCV data

* Synchronize timestamps across symbols

* Generate spread series: Spread(t) = Price_A(t) - β × Price_B(t)

* Stationarity testing (ADF) and Johansen test for cointegration


### 🔍 4. Model Calibration (OU Process)
Model:
OU Process:
      dXₜ = θ(μ - Xₜ)dt + σ dWₜ

Estimate parameters (θ, μ, σ) using MLE on spread series.

Estimate half-life: ln(2)/θ to determine holding horizon.

### 📈 5. Signal Generation
*Z-Score Strategy:*
* Entry signal: Z-score exceeds upper/lower threshold

* Exit: Z-score reverts to mean

*Trading Logic*:
* Long spread: if z-score < -entry threshold

* Short spread: if z-score > +entry threshold

* Exit: abs(z-score) < 0.1

### ⚙️ 6. Backtesting and Execution Simulation
*Features:*

* Simulate execution with fill probability
* Apply realistic transaction cost (e.g., 2 bps per leg)
* Daily capital constraint
* Trade sizing via z-score magnitude or volatility scaling

### 📊 7. Performance Evaluation
*Metrics:*
* Sharpe Ratio
* Annualized PnL
* Max Drawdown
* Return on Margin (ROM): PnL / max capital deployed
* Win rate, Trade count, Avg holding time

### 🔎 8. Result Summary
<img width="509" height="341" alt="image" src="https://github.com/user-attachments/assets/0c5aeb21-1fb5-47db-b53e-b1c06a95f6ff" />

### 🧪 9. Robustness Checks
* Walk-forward calibration
* Rolling cointegration windows
* Slippage sensitivity
* Stress-test performance under spread breakdown

### 🛠️ 10. Improvements and Next Steps
* Add stop-loss layer based on rolling volatility
* Adapt strategy for live trading on API (e.g., Zerodha Kite Connect)
* Introduce LSTM-based OU parameter forecasting (for research only)
* Explore multi-pair optimization or pair rotation
