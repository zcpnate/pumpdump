Python Bittrex Pump and Dumper
=

Uses Python 2.7.x.

Tested on OS X 10.12.5, and Windows 7 x64.

This program will allow you to type the name of a coin when a Telegram
Pump and Dump group says the name, and it will automatically place a
buy order at +X%*ask, and a sell order at +Y%*buy-price.


Usage
=
  Add your API key and secret to pumpdump.py.

  !!! Ensure you do not enable withdraws or market trading !!!

  Although this script doesn't do anything regarding withdraws or
  market trading (you can see for yourself in the code...), it is best
  practice not to give any program more access than it needs.

  Example:
  
    $ python pumpdump.py -h
    usage: pumpdump.py [-h] [-o] -b BUY -s SELL (-c COIN | -p)

    Python Pump and Dumper

    Buys max amount of a specified coin at a percent above the current ask,
    and immidiately places a sell order at a percent above the price bought
    at.

    optional arguments:
      -h, --help            show this help message and exit
      -o, --order           Enables Trading... Be careful..
      -b BUY, --buy BUY     Sets the percentage above current ask to buy (int 0-99)
      -s SELL, --sell SELL  Sets the percentage above the buy price to sell (int 0-99)
      -c COIN, --coin COIN  Sets the coin name
      -p, --prompt          Prompts user for coin name.


TODO
=

Probably could format the code better, just wanted to get basic functionality up first.

"telegram is laggy as shit, better to check the bittrex home page for coins that fly up in % in the last min they announce" - @Andre#0370

Credits
=

https://github.com/ndri/python-bittrex

Donate
=

If you feel like this program helped you out, or made you money, feel free to donate!

BTC: 1Gv2MDC8YgjDYiy6P7sTZizihEKoJyK8ew

This is free and always will be
=

Fuck this guy trying to charge people for my open sourced script.

@zaizoun 

![Fuck zaizoun](https://cdn.discordapp.com/attachments/330399816322514966/330531841566310401/slack.PNG)

![Fuck zaizoun2](https://cdn.discordapp.com/attachments/330399816322514966/330531959853940746/2.0.PNG)


Disclaimer
=

USE AT OWN RISK

PROFITS NOT GUARENTEED

!!! Ensure you do not enable withdraws or market trading !!!

Although this script doesn't do anything regarding withdraws or
market trading (you can see for yourself in the code...), it is best
practice not to give any program more access than it needs.

