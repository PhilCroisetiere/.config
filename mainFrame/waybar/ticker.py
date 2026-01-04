import argparse
import yfinance as yf
from termcolor import colored
import time
import pandas as pd
def get_stock_price_and_change(ticker):
    try:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d", interval="1m")
        yesterday = stock.history(period="1d", interval="1m", start=history.index[0] - pd.Timedelta(days=1), end=history.index[0])
        history.index[0] - pd.Timedelta(days=1) 
        if len(history) < 1:
            return None, None
        opening_price = history['Open'].iloc[0]  # Get the opening price of the day
        current_close = history['Close'].iloc[-1]  # Get the most recent closing price
        yesterday_close = yesterday['Close'].iloc[-1] if not yesterday.empty else opening_price
        percent_change = ((current_close - yesterday_close) / yesterday_close) * 100
        return current_close, percent_change
    except Exception as e:
        return None, None

def main():
    parser = argparse.ArgumentParser(description="CLI tool to fetch stock prices from Yahoo Finance.")
    parser.add_argument('tickers', nargs='+', help="List of stock tickers to fetch prices for.")
    args = parser.parse_args()

    tickers = args.tickers
      # Spread updates evenly within a minute

    for ticker in tickers:
        price, change = get_stock_price_and_change(ticker)
        if price is not None and change is not None:
            arrow = "↑" if change > 0 else "↓"
            color = "green" if change > 0 else "red"
            print(f"{ticker}: {colored(arrow, color)} {price:.2f} ({colored(f'{change:+.2f}', color)}%)", flush=True)
        else:
            print(f"{ticker}: {colored('Error fetching data', 'yellow')}", flush=True)

if __name__ == "__main__":
    main()
