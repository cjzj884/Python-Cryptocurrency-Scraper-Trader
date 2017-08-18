#!/usr/bin/env python
# This program buys some Dogecoins and sells them for a bigger price
from bittrex3.bittrex3 import Bittrex3
from forex_python.bitcoin import BtcConverter
import json


b = BtcConverter()

latestBitcoinPrice = b.get_latest_price('USD')
print("Latest Bitcoin Price " + str(latestBitcoinPrice))

dollarsToUSD = b.convert_to_btc(1, "USD")
print("1 USD to bitcoin " + str(dollarsToUSD))

# Get these from https://bittrex.com/Account/ManageApiKey
#api = Bittrex3('ecf839a28fcf46889cc1f8cc95ec05c6', 'fb0d5e1aee744a7997f3dfa43b18cc57')

with open("secrets.json") as secrets_file:
    secrets = json.load(secrets_file)
    secrets_file.close()

api = Bittrex3(secrets['key'], secrets['secret'])



# Market to trade at
trade = 'BTC'
currency = 'DOGE'
market = '{0}-{1}'.format(trade, currency)

# Amount of coins to buy
amount = 1

# How big of a profit you want to make
multiplier = 1.1

# Getting the BTC price for DOGE
dogesummary = api.get_ticker(market)

dogeprice = dogesummary['result']['Last']

print ('The price for {0} is {1:.8f} {2}.'.format(currency, dogeprice, trade))

# Buying 100 DOGE for BTC
print ('Buying {0} {1} for {2:.8f} {3}.'.format(amount, currency, dogeprice, trade))
api.buylimit(market, amount, dogeprice)

# Multiplying the price by the multiplier
dogeprice = round(dogeprice*multiplier, 8)

# Selling 100 DOGE for the  new price
print ('Selling {0} {1} for {2:.8f} {3}.'.format(amount, currency, dogeprice, trade))
api.selllimit(market, amount, dogeprice)

# Gets the DOGE balance
dogebalance = api.getbalance(currency)
print ("Your balance is {0} {1}.".format(dogebalance['Available'], currency))

# For a full list of functions, check out bittrex.py or https://bittrex.com/Home/Api