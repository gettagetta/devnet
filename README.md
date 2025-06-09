# devnet

This repository contains a simple stock analysis script.

## Setup

Install the required dependencies:

```bash
pip install yfinance matplotlib
```

## Usage

Run the script with a ticker symbol and date range:

```bash
python stock_analysis.py --symbol AAPL --start 2020-01-01 --end 2020-12-31
```

This will print the first rows of the data with 20-day moving average and show a plot.
