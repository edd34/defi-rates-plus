# Defi Rate Plus

This project leverage Selenium and Python in order to scrap lending/borrowing rate from [Defi Rate](https://defirate.com/lend/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

## Example result
Result is sorted by rates
```json
[{'name': 'Bitfinex', 'rates': 94.31, 'token': 'EOS'},
 {'name': 'Bitfinex', 'rates': 48.96, 'token': 'YFI'},
 {'name': 'Bitfinex', 'rates': 43.94, 'token': 'ETC'},
 {'name': 'Bitfinex', 'rates': 33.56, 'token': 'ZRX'},
 {'name': 'Aave', 'rates': 32.55, 'token': 'SUSD'},
 {'name': 'Bitfinex', 'rates': 31.27, 'token': 'UNI'},
 {'name': 'Bitfinex', 'rates': 25.86, 'token': 'BTG'},
 {'name': 'Bitfinex', 'rates': 16.12, 'token': 'BSV'},
 {'name': 'Celsius', 'rates': 13.99, 'token': 'MATIC'},
 {'name': 'Celsius', 'rates': 13.99, 'token': 'SNX'},
 {'name': 'Bitfinex', 'rates': 13.31, 'token': 'ETH'},
 {'name': 'Aave', 'rates': 11.76, 'token': 'USDT'},
 {'name': 'Nexo', 'rates': 10.0, 'token': 'DAI'},
 {'name': 'Nexo', 'rates': 10.0, 'token': 'USDC'},
 {'name': 'Celsius', 'rates': 10.0, 'token': 'BUSD'},
 {'name': 'Celsius', 'rates': 10.0, 'token': 'GUSD'},
 {'name': 'Nexo', 'rates': 10.0, 'token': 'PAX'},
 {'name': 'Nexo', 'rates': 10.0, 'token': 'TUSD'},
 {'name': 'Celsius', 'rates': 10.0, 'token': 'ZUSD'},
 {'name': 'Celsius', 'rates': 8.86, 'token': 'DOT'},
 {'name': 'Bitfinex', 'rates': 7.38, 'token': 'LTC'},
 {'name': 'Nexo', 'rates': 6.0, 'token': 'BTC'},
 {'name': 'Coinbase', 'rates': 6.0, 'token': 'ALGO'},
 {'name': 'Nexo', 'rates': 6.0, 'token': 'BCH'},
 {'name': 'Nexo', 'rates': 6.0, 'token': 'LINK'},
 {'name': 'Nexo', 'rates': 6.0, 'token': 'XRP'},
 {'name': 'Celsius', 'rates': 5.92, 'token': 'AAVE'},
 {'name': 'Celsius', 'rates': 5.5, 'token': 'BNT'},
 {'name': 'Celsius', 'rates': 5.5, 'token': 'DASH'},
 {'name': 'Celsius', 'rates': 5.5, 'token': 'PAXG'},
 {'name': 'Celsius', 'rates': 5.5, 'token': 'XAUT'},
 {'name': 'Celsius', 'rates': 4.86, 'token': 'CEL'},
 {'name': 'Coinbase', 'rates': 4.63, 'token': 'XTZ'},
 {'name': 'Celsius', 'rates': 4.6, 'token': 'COMP'},
 {'name': 'Celsius', 'rates': 4.51, 'token': 'UMA'},
 {'name': 'dYdX', 'rates': 4.41, 'token': 'SAI'},
 {'name': 'Celsius', 'rates': 3.51, 'token': 'BAT'},
 {'name': 'Celsius', 'rates': 3.1, 'token': 'XLM'},
 {'name': 'Celsius', 'rates': 2.53, 'token': 'KNC'},
 {'name': 'Bitfinex', 'rates': 2.09, 'token': 'OMG'},
 {'name': 'Celsius', 'rates': 2.02, 'token': 'MANA'},
 {'name': 'Celsius', 'rates': 2.02, 'token': 'ZEC'},
 {'name': 'Fulcrum', 'rates': 1.56, 'token': 'WBTC'},
 {'name': 'Fulcrum', 'rates': 1.28, 'token': 'LRC'},
 {'name': 'Bitfinex', 'rates': 0.15, 'token': 'ADA'},
 {'name': 'Aave', 'rates': 0.01, 'token': 'LEND'}]
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)