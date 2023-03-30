from api.binance import API_KEY_BINANCE, API_SECRET_KEY_BINANCE
from binance.client import Client
import json

client = Client(API_KEY_BINANCE, API_SECRET_KEY_BINANCE)

ticker = client.get_symbol_ticker(symbol='BTCUSDT')
price = ticker['price']

data = json.dumps(ticker, indent=4)
print(f"The current price of BTC is: {price} USD")
print(data)