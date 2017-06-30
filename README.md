Python Bittrex Pump and Dumper
=

Uses Python 2.7.x.

Tested on OS X 10.12.5, and Windows 7 x64.

This program will allow you to type the name of a coin when a Telegram
Pump and Dump group says the name, and it will automatically place a
buy order at +10%*ask, and a sell order at +30%*ask. You can change
these values, but they seem like they will provide safe steady income.


Usage
=
  Add your API key and secret to pumpdump.py.

  !!! Ensure you do not enable withdraws or market trading !!!

  Although this script doesn't do anything regarding withdraws or
  market trading (you can see for yourself in the code...), it is best
  practice not to give any program more access than it needs.

  Also, make note of the `allow_order` variable. If set to `True`, it
  will buy and sell coins. `False`, it will just display values.

  Example:

    $ python pumpdump.py
			!!! BY DEFAULT THIS WILL BUY AS MANY COINS AS YOU HAVE BTC AVAILABLE !!!
			!!! PRESS CTRL+C TO CANCEL BEFORE TYPING ANY COIN NAMES IF YOU DON"T WANT TO BUY !!!

			Coin: ETH
			You have 0.00137032 BTC available.
			Ask -- 0.11681
			Ask + 10% (safeish buy point) -- 0.128491
			Ask + 30% (safeish sell point) -- 0.151853

			[+] Buying 0.0114379077134 ETH coins at 0.128491 BTC each for a total of 0.0014696682 BTC
      {u'uuid': u'4dceb026-23ef-483a-294e-eb5ce94dbe7c'}
			[+] Placing sell order at 0.151853 (+30%)...
      {u'uuid': u'4dceb026-23ef-483a-294e-eb5ce94dbe7c'}

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

Disclaimer
=

USE AT OWN RISK

PROFITS NOT GUARENTEED

!!! Ensure you do not enable withdraws or market trading !!!

Although this script doesn't do anything regarding withdraws or
market trading (you can see for yourself in the code...), it is best
practice not to give any program more access than it needs.

