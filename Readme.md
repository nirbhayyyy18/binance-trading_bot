# Binance Futures Testnet Trading Bot

Python CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Setup

1 Install dependencies

pip install -r requirements.txt

2 Create .env file

API_KEY=your_api_key
API_SECRET=your_api_secret

3 Run bot

Market Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

Limit Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 65000