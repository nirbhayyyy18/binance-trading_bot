# Binance Futures Testnet Trading Bot

## Project Description

This project is a simple Python CLI trading bot that places orders on the Binance Futures Testnet (USDT-M).
It supports MARKET and LIMIT orders for both BUY and SELL sides.
The application follows a structured architecture with separate client, order logic, validation, and CLI layers.
It also includes logging and error handling for API requests and responses.

---

## Setup Steps

1. Clone the repository

git clone https://github.com/your-username/trading_bot.git
cd trading_bot

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows (PowerShell)

.\venv\Scripts\Activate

Mac / Linux

source venv/bin/activate

4. Create a `.env` file in the project root and add your Binance Testnet API credentials

API_KEY=your_api_key
API_SECRET=your_api_secret

You can generate API credentials from Binance Futures Testnet.

---

## Install Dependencies

pip install -r requirements.txt

---

## How to Run the Bot

The bot accepts inputs from the command line.

Required parameters:

symbol
side (BUY / SELL)
order_type (MARKET / LIMIT)
quantity
price (required only for LIMIT orders)

---

## Example Usage

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.002

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.002 --price 66000

---

## Example Output

Order Request Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

Order Response
Order ID: 123456789
Status: FILLED
Executed Qty: 0.002
Avg Price: 65100

Order placed successfully.

---

## Logging

All API requests, responses, and errors are logged into a log file:

bot.log

The log file includes records of both MARKET and LIMIT order executions.

---

## Project Structure

trading_bot/

bot/
├── client.py
├── orders.py
├── validators.py
├── logging_config.py

cli.py
README.md
requirements.txt

---

## Assumptions

* Binance Futures Testnet account is already created.
* API keys are configured in the `.env` file.
* Orders follow Binance minimum notional requirements.
