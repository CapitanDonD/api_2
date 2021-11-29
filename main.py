import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def shorten_link(bitly_token, url):
    payload =  {"long_url": url}
    attribute_url = "https://api-ssl.bitly.com/v4/bitlinks"
    response = requests.post(attribute_url, headers=bitly_token, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(bitly_token, bitlink):
    parsed_bitlink = urlparse(bitlink)
    bitlink_without_scheme = f"{parsed_bitlink.netloc}{parsed_bitlink.path}"
    attribute_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink_without_scheme}/clicks/summary"
    response = requests.get(attribute_url, headers=bitly_token)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(bitly_token, url):
    parsed_url = urlparse(url)
    url_without_scheme = f"{parsed_url.netloc}{parsed_url.path}"
    attribute_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url_without_scheme}/clicks/summary"
    response = requests.get(attribute_url, headers=bitly_token)
    return response.ok


if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(
    description='Эта программа переобразовавыет битлинк и может показать клики по нему'
    )
    parser.add_argument('url_or_bitly', help='Битлинк или ссылка')
    args = parser.parse_args()
    bitly_token = os.getenv("BITLY_TOKEN")
    authorization = {"Authorization" : f"Bearer {bitly_token}"}

    if is_bitlink(authorization, args.url_or_bitly):
        try:
            clicks_bitlink = count_clicks(authorization, args.url_or_bitly)
            print(f"Колличество кликов по ссылке: {clicks_bitlink}")
        except requests.exceptions.HTTPError:
            print("Ошибка при подсчётывании кликов")
    else:
        try:
            bitlink = shorten_link(authorization, args.url_or_bitly)
            print(bitlink)
        except requests.exceptions.HTTPError:
            print("Ошибка при сокращении ссылки")

    print(args.url_or_bitly)
