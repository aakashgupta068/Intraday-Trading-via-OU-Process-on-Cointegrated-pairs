import matplotlib.pyplot as plt

def plot_spread_with_signals(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['spread'], label='Spread')
    plt.fill_between(df.index, df['spread'], where=df['mod_position']==1, color='green', alpha=0.3, label='Short Spread')
    plt.fill_between(df.index, df['spread'], where=df['mod_position']==-1, color='red', alpha=0.3, label='Long Spread')
    plt.legend()
    plt.title("Spread and Trade Zones")
    plt.grid(True)
    plt.show()

def plot_equity(df):
    df['cumulative_pnl'].plot(title='Cumulative PnL', figsize=(12, 4))
    plt.grid(True)
    plt.show()