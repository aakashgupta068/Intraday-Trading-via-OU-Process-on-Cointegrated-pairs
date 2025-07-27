import pandas as pd
import numpy as np
from data_loader import download_intraday_data
from cointegration import get_cointegration_vector, adf_test
from ou_model import estimate_ou_parameters
from signal_generator import generate_signals
from backtester import compute_positions, compute_pnl, compute_metrics
from visualizer import plot_spread_with_signals, plot_equity

# Download data
tickers = ['AAPL', 'MSFT']
data = download_intraday_data(tickers)
log_A = data['AAPL']['Close'].apply(np.log)
log_B = data['MSFT']['Close'].apply(np.log)
df = pd.DataFrame({'log_A': log_A, 'log_B': log_B}).dropna()

# Cointegration
beta = get_cointegration_vector(df[['log_A', 'log_B']])
df['spread'] = df['log_A'] - beta[1] * df['log_B']
if adf_test(df['spread']) > 0.05:
    print("Spread is not stationary")
    exit()

# OU calibration
mu, theta, sigma, half_life = estimate_ou_parameters(df['spread'])
print(f"OU Params: mu={mu}, theta={theta}, sigma={sigma}, half_life={half_life}")

# Signal generation
df = generate_signals(df, mu, sigma, upper=1.25, lower=0.4, half_life=int(half_life))

# Backtest
df = compute_positions(df)
df = compute_pnl(df)
metrics = compute_metrics(df)
print("Backtest Metrics:", metrics)

# Visualization
plot_spread_with_signals(df)
plot_equity(df)