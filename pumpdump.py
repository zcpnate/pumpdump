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

# Set to True to enable limit trading...
# !!! USE AT OWN RISK !!!
allow_orders = False

def sigint_handler(signum, frame):
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
askTen = askPrice + (0.1 * askPrice)
askThirty = askPrice + (0.3 * askPrice)

btcBalance = api.getbalance("BTC")['Available']

print 'You have {} BTC available.'.format(btcBalance)
print 'Ask -- ' + str(askPrice)
print 'Ask + 10% (safeish buy point) -- ' + str(askTen)
print 'Ask + 30% (safeish sell point) -- ' + str(askThirty)

numCoins = (btcBalance - (btcBalance*0.0025)) / askTen

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
