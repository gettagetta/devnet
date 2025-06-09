import argparse
import sys

try:
    import yfinance as yf
    import matplotlib.pyplot as plt
except ImportError as e:
    print("Required packages are missing: {}".format(e))
    sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(description="Simple stock analysis tool")
    parser.add_argument('--symbol', required=True, help='Ticker symbol, e.g., AAPL')
    parser.add_argument('--start', required=True, help='Start date YYYY-MM-DD')
    parser.add_argument('--end', required=True, help='End date YYYY-MM-DD')
    return parser.parse_args()


def main():
    args = parse_args()
    data = yf.download(args.symbol, start=args.start, end=args.end)
    if data.empty:
        print("No data found for symbol {}".format(args.symbol))
        return

    data['Return'] = data['Adj Close'].pct_change()
    data['MA20'] = data['Adj Close'].rolling(window=20).mean()

    print(data[['Adj Close', 'Return', 'MA20']].dropna().head())

    data[['Adj Close', 'MA20']].plot(title=f'{args.symbol} Adj Close and 20-day MA')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
