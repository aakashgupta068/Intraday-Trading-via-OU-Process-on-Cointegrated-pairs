import numpy as np

def generate_signals(df, mu, sigma, upper, lower, half_life, cooldown=2):
    df['zscore'] = (df['spread'] - mu) / sigma
    df['trade_signal'] = "neutral"
    df.loc[df['zscore'] > upper, 'trade_signal'] = 'long-spread'
    df.loc[df['zscore'] < -upper, 'trade_signal'] = 'short-spread'
    df.loc[abs(df['zscore']) < lower, 'trade_signal'] = 'exit-trade'
    df['mod_signal'] = df['trade_signal'].copy()

    i = 0
    while i < len(df):
        signal = df.iloc[i]['trade_signal']
        if signal in ['long-spread', 'short-spread']:
            j = i + 1
            while j < len(df) and df.iloc[j]['trade_signal'] == signal:
                if (j - i) >= half_life:
                    break
                j += 1
            if j < len(df) and df.iloc[j]['trade_signal'] == signal:
                df.iloc[j, df.columns.get_loc('mod_signal')] = 'exit-trade'
                df.iloc[j+1: j+1+cooldown, df.columns.get_loc('mod_signal')] = 'neutral'
            i = j + 1
        else:
            i += 1
    return df