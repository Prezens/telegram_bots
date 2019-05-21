import requests
from main import write_json
import re


def parse_text():
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    print(crypto)


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v2/ticker/{}/'.format(crypto)
    r = requests.get(url).json()
    price = r['data']['quotes']['USD']['price']
    # write_json(r.json(), filename='price.json')

    return price


def main():
    # print(get_price())
    parse_text('сколько стоит /bitcoin')


if __name__ == '__main__':
    main()
