import numpy as np

def compute_positions(df):
    position_map = {
        'long-spread': -1,
        'short-spread': 1,
        'exit-trade': 0,
        'neutral': np.nan
    }
    df['mod_position'] = df['mod_signal'].map(position_map).ffill().fillna(0)
    return df

def compute_pnl(df):
    df['spread_return'] = df['spread'].diff().fillna(0)
    df['pnl'] = df['mod_position'].shift(1) * df['spread_return']
    df['cumulative_pnl'] = df['pnl'].cumsum()
    return df

def compute_metrics(df):
    mean_ret = df['pnl'].mean()
    std_ret = df['pnl'].std()
    sharpe = (mean_ret / std_ret) * np.sqrt(252 * 390)
    intraday_sharpe = (mean_ret / std_ret) * np.sqrt(len(df))
    total_pnl = df['cumulative_pnl'].iloc[-1]
    max_dd = (df['cumulative_pnl'] - df['cumulative_pnl'].cummax()).min()
    total_profit = df['pnl'][df['pnl'] > 0].sum()
    total_loss = df['pnl'][df['pnl'] < 0].sum()
    profit_ratio = total_profit / abs(total_loss) if total_loss != 0 else np.inf

    return {
        'sharpe_ratio': sharpe,
        'intraday_sharpe': intraday_sharpe,
        'total_pnl': total_pnl,
        'max_drawdown': max_dd,
        'profit_ratio': profit_ratio
    }