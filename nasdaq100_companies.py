import csv
import http
import pathlib

import pandas as pd
import requests


NASDAQ100_URL = 'https://api.nasdaq.com/api/quote/list-type/nasdaq100'
NASDAQ100_HEADERS = {
    'dnt': '1', 
    'upgrade-insecure-requests': '1', 
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}


def get_constituents() -> dict:
    response = requests.get(NASDAQ100_URL, headers=NASDAQ100_HEADERS)
    response.raise_for_status()
    if response.status_code != http.HTTPStatus.OK:
        error_str = "Expected HTTP status code 200 but got {}".format(
            response.status_code)
        raise requests.exceptions.HTTPError(error_str)
    
    resp_json = response.json()
    if resp_json['data'] is None:
        raise TypeError("Expected data of type dict but got NoneType object")

    return resp_json


def update_constituents() -> None:
    try:
        data_json = get_constituents()
    except request.exceptions.RequestException as e:
        raise SystemExit(e)
    except TypeError as e:
        raise SystemExit(e)

    nasdaq100_constituents = data_json['data']['data']['rows']
    constituents = [
        (c['symbol'],c['companyName']) for c in nasdaq100_constituents
    ]

    sorted_constituents = sorted(constituents, key=lambda x: x[0])
    sorted_symbols = [x for (x,y) in sorted_constituents]

    save_constituents(sorted_constituents, sorted_symbols)


def save_constituents(constituents: list, symbols: list) -> None:
    output_path = pathlib.Path('./data')
    try:
        output_path.mkdir(parents=True, exist_ok=True)

        pd.DataFrame(constituents).to_csv(
            output_path.joinpath('nasdaq100_constituents.csv'),
            header=['Symbol', 'Name'],
            index=False,
            quoting=csv.QUOTE_ALL
        )

        pd.DataFrame(symbols).to_csv(
            output_path.joinpath('nasdaq100_symbols.csv'),
            header=False,
            index=False
        )
    except OSError as e:
        raise SystemExit(e)


if __name__ == '__main__':
    update_constituents()
