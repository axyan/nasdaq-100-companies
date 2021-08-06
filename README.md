# NASDAQ-100 Companies
NASDAQ-100 Companies is a script that updates and saves the constituents of the
NASDAQ-100 index and their symbols. The NASDAQ-100 index includes the top 100
largest non-financial companies listed on the NASDAQ stock exchange based on
market capitalization. The NASDAQ-100 index is popular due to its heavy tech
focus and is tracked by other popular ETFs such as the QQQ by Invesco.

## Installation

The script requires some external Python libraries.

```bash
pip install -r scripts/requirements.txt
```

## Usage

By default, the script will create a local 'data' directory. The script will 
save a file with the constituents and another file with the symbols of the 
constituents.

```bash
python scripts/nasdaq100_constituents.py
```

## License

All code is licensed under the [MIT license](https://github.com/axyan/nasdaq-100-companies/blob/main/LICENSE).
