import yfinance as yf
import time

while True:
    ticker = yf.Ticker("AAPL")
    df = ticker.history(period='1d')
    price = df.iloc[-1]['Close']
    print(f'Current price of AAPL: {price}')
    time.sleep(60)




