#!/usr/bin/env python

"""Python Pump and Dumper

This program allows you to input a cryptocoin name and it will
calculate a buy point 10% higher than the current 'ask', and a sell
point at 30% higher than the current 'ask'. While not making a ton of
profit each time, typing the coin name is much quicker than navigating
to Bittrex and manually buying and selling. It will be small, but safe
profit.

!!! BY DEFAULT THIS WILL BUY AS MANY COINS AS YOU HAVE BTC AVAILABLE !!!

Note: This is not guarenteed to make any profit. The markets are
volitile, and even if a pump is happening, it is possible that it
could not reach +30%, and thus you could be stuck with worthless coins
if you don't sell fast enough.
"""

from bittrex import bittrex
import sys, signal, json

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('key', 'secret')

# do before entering coin to save the API call during the pump
btcBalance = api.getbalance("BTC")['Available']

# Set to True to enable limit trading...
# !!! USE AT OWN RISK !!!
allow_orders = False

def sigint_handler(signum, frame):
    """Handler for ctrl+c"""
    print '\n[!] CTRL+C pressed. Exiting...'
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if allow_orders:
    print '!!! BY DEFAULT THIS WILL BUY AS MANY COINS AS YOU HAVE BTC AVAILABLE !!!'
    print '!!! PRESS CTRL+C TO CANCEL BEFORE TYPING ANY COIN NAMES IF YOU DON"T WANT TO BUY !!!\n'
else:
    print "[!] allow_orders = False in script... change to make orders..."

pumpCoin = raw_input("Coin: ")

coinPrice = api.getticker("BTC-" + pumpCoin)
askPrice = coinPrice['Ask']

# 10%/30% are arbitrary numbers, change to suit you
askTen = askPrice + (0.1 * askPrice)
askThirty = askPrice + (0.3 * askPrice)

print 'You have {} BTC available.'.format(btcBalance)
print 'Current ask price for {} is {} BTC.'.format(pumpCoin, askPrice)
print 'Ask + 10% (safeish buy point) for {} is {} BTC.'.format(pumpCoin, askTen)
print 'Ask + 30% (safeish sell point) for {} is {} BTC.'.format(pumpCoin, askThirty)

# calculates the number of pumpCoin(s) to buy, taking into
# consideration Bittrex's 0.25% fee.
numCoins = (btcBalance - (btcBalance*0.00251)) / askTen

buyPrice = askTen * numCoins
sellPrice = askThirty * numCoins
profit = sellPrice - buyPrice

print '\n[+] Buying {} {} coins at {} BTC each for a total of {} BTC'.format(numCoins,
        pumpCoin, askTen, buyPrice)

if allow_orders:
    print api.buylimit('BTC-' + pumpCoin, numCoins, askTen)
else:
    print "[!] allow_orders = False in script... change to make orders..."

print '[+] Placing sell order at {} (+30%)...'.format(askThirty)

if allow_orders:
    print api.selllimit('BTC-' + pumpCoin, numCoins, askThirty)
else:
    print "[!] allow_orders = False in script... change to make orders..."

print '[+] Sold {} {} coins at {} BTC each for a total of {} BTC'.format(numCoins, pumpCoin, askThirty, sellPrice)

print '[+] Profit: {} BTC'.format(profit)
