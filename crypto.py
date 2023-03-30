import requests
from datetime import datetime
import api.binance as api
import json

class Crypto:
    def __init__(self, coin, currency='USDT'):
        self.coin = coin
        self.currency = currency
        self.symbol = coin+currency
        self.price = self.update_price_from_binance()
        self.last_updated = datetime.now()
    
    def update_sysdate(self):
        self.last_updated = datetime.now()

    def printall(self):
        print('Coin: ' + self.coin)
        print('Currency: ' + self.currency)
        print('Symbol: ' + self.symbol)
        print('Price: ' + str(self.price))
        print('Last updated at: ' + self.last_updated.strftime("%Y-%m-%d %H:%M:%S"))

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        self.update_sysdate()

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        self.update_sysdate()
    
    def update_price_from_binance(self):
        endpoint = api.PRICE_ENDPOINT
        params = {"symbol":self.symbol}
        response = requests.get(endpoint, params=params).json()
        price = response['price']
        self.price = float(price)
        print(f'Price for {self.symbol} updated to {self.price} successfully.')
        self.update_sysdate()


crypto = Crypto('BTC','GBP')
# crypto.update_price_from_binance()
crypto.printall()


