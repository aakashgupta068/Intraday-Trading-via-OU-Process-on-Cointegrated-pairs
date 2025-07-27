import yfinance as yf

def download_intraday_data(tickers, days=7):
    return yf.download(tickers=tickers, period=f"{days}d", interval="1m", group_by='ticker', prepost=True)