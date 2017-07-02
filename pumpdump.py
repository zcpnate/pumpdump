#!/usr/bin/env python

"""Python Pump and Dumper

This program allows you to input a cryptocoin name and it will
calculate a buy point x% higher than the current 'ask', and a sell
point at y% higher than the buy price. While not making a ton of
profit each time, typing the coin name is much quicker than navigating
to Bittrex and manually buying and selling. It will be small, but safe
profit.

Note: This is not guarenteed to make any profit. The markets are
volitile, and even if a pump is happening, it is possible that it
could not reach +30%, and thus you could be stuck with worthless coins
if you don't sell fast enough.
"""

from bittrex import bittrex

import sys
import signal
import json
import argparse

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('key', 'secret')


def getArgs():
    """Parses command line arguments."""

    # indentation for formating
    parser = argparse.ArgumentParser(
        description='''
Python Pump and Dumper

Buys max amount of a specified coin at a percent above the current ask,
and immidiately places a sell order at a percent above the price bought
at.''', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
            '-o',
            '--order',
            help='Enables Trading... Be careful..',
            action="store_true",
            dest="allow_orders",
            default=False)

    parser.add_argument(
            '-b',
            '--buy',
            help='Sets the percentage above current ask to buy (int 0-99)',
            type=int,
            dest='buy',
            required=True)

    parser.add_argument(
            '-s',
            '--sell',
            help='Sets the percentage above the buy price to sell (int 0-99)',
            type=int,
            dest='sell',
            required=True)

    # prompt or specify coin in command line
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--coin', help='Sets the coin name', dest='coin')
    group.add_argument(
            '-p', '--prompt', help='Prompts user for coin name.',
            action='store_true', dest='coin')

    args = parser.parse_args()

    return args.allow_orders, args.coin, args.buy, args.sell


def sigint_handler(signum, frame):
    """Handler for ctrl+c"""

    print '\n[!] CTRL+C pressed. Exiting...'
    sys.exit(0)


def buy_coins(api, coin, num_coins, price):
    """Places a buy limit order on Bittrex"""
    return api.buylimit('BTC-{}'.format(coin), num_coins, price)


def sell_coins(api, coin, num_coins, price):
    """Places a sell limit order on Bittrex"""
    return api.selllimit('BTC-{}'.format(coin), num_coins, price)

if __name__ == '__main__':
    # get cmd args
    allow_orders, pump_coin, buy_percent, sell_percent = getArgs()

    # setup ctrl+c handler
    signal.signal(signal.SIGINT, sigint_handler)

    # do before entering coin to save the API call during the pump
    btc_balance = api.getbalance("BTC")['Available']

    if allow_orders:
        print '!!! BY DEFAULT THIS WILL BUY AS MANY COINS AS YOU HAVE BTC !!!'
        print '!!! PRESS CTRL+C TO CANCEL !!!\n'
    else:
        print '[!] Trading disabled'

    # prompt for coin
    # test if pump_coin is bool since checking if == True would give
    # a type error if it's set to the coin name
    if isinstance(pump_coin, bool):
        pump_coin = raw_input("[?] Coin: ")

    coin_price = api.getticker("BTC-" + pump_coin)['Ask']

    buy_price = coin_price + ((float(buy_percent) / 100) * coin_price)
    sell_price = buy_price + ((float(sell_percent) / 100) * buy_price)

    print '[+] {} BTC available'.format(btc_balance)
    print '[+] {} ask price is {} BTC'.format(pump_coin, coin_price)
    print '[+] +{}% for {} at {} BTC'.format(
            buy_percent, pump_coin, buy_price)
    print '[+] +{}% for {} at {} BTC'.format(
            sell_percent, pump_coin, sell_price)

    # calculates the number of pump_coin(s) to buy, taking into
    # consideration Bittrex's 0.25% fee. (plus a little bit in case of
    # 0.00000001btc probs?)
    num_coins = (btc_balance - (btc_balance * 0.00251)) / buy_price

    buy_cost = buy_price * num_coins
    sell_cost = sell_price * num_coins
    profit = sell_cost - buy_cost

    print '[+] Buying {} {} coins at {} BTC each for a total of {} BTC'.format(
            num_coins, pump_coin, buy_price, buy_cost)

    if allow_orders:
        print '[!] {}'.format(buy_coins(api, pump_coin, num_coins, buy_price))
    else:
        print '[!] Trading disabled'

    print '[+] Placing sell order at {} (+{}%)...'.format(
            sell_price, sell_percent)

    if allow_orders:
        print '[!] {}'.format(sell_coins(api, pump_coin, num_coins, sell_price))
    else:
        print '[!] Trading disabled'

    print '[+] Sold {} {} coins at {} BTC each for a total of {} BTC'.format(
            num_coins, pump_coin, sell_price, sell_cost)

    print '[+] Profit: {} BTC'.format(profit)
