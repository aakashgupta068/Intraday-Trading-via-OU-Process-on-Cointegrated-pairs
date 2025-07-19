# Intraday-Trading-via-OU-Process-on-Cointegrated-pairs
Modeled mean-reverting intraday spreads using the Ornstein-Uhlenbeck process on Johansen cointegrated pairs. Optimized MLE parameters with vectorized computation on 5-min data. Backtested using Backtrader with 2.2 Sharpe, 15% PnL, and 60% win rate over one year.

🧾 1. Project Title and Abstract
📌 Title:
Intraday OU-Based Pairs Trading on NSE: Mean-Reverting Signal with Cost-Aware Execution

📄 Abstract:
This project models intraday spreads between cointegrated equity pairs using the Ornstein-Uhlenbeck (OU) process to identify mean-reverting trade opportunities. Parameters are calibrated via Maximum Likelihood Estimation (MLE), and the strategy is validated using realistic fill assumptions, transaction costs, and capital management rules. Performance is evaluated using Sharpe ratio, annualized PnL, ROM, and drawdown.

📁 2. Directory Structure
bash
Copy
Edit
├── data/                  # Raw and processed market data
├── notebooks/             # EDA, modeling, performance analysis
├── src/
│   ├── data_loader.py     # Load & preprocess data \n
│   ├── cointegration.py   # Pair filtering via Johansen test
│   ├── ou_model.py        # OU parameter estimation
│   ├── signal_engine.py   # Z-score logic, entry/exit rules
│   ├── backtest_engine.py # Execution logic and capital tracking
│   └── metrics.py         # Sharpe, drawdown, ROM calculations
├── requirements.txt
├── README.md
└── main.py
