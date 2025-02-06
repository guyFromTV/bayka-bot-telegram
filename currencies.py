import requests
from decimal import Decimal

RUB_TO_AZN = 0.019

ERROR_FETCHING_VALUE = -1
INCORRECT_FROM_CURRENCY_ERROR = -2
INCORRECT_TO_CURRENCY_ERROR = -3

CURRENCY_API_URL = (
    "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api"
    "@2024-03-06/v1/currencies/{currency}.json"
)

CURRENCY_LIST_API_URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"


def get_all_available_currencies():
    response = requests.get(CURRENCY_LIST_API_URL)
    if response.status_code == 200:
        return response.json()
    return {}


def is_currency_available(currency: str) -> bool:
    return currency.lower() in get_all_available_currencies()

def get_currency_ratio(from_currency, to_currency):
    from_currency = from_currency.lower()
    to_currency = to_currency.lower()
    url = CURRENCY_API_URL.format(currency=from_currency)
    response = requests.get(url)
    if response.status_code != 200:
        if response.status_code == 404:
            return INCORRECT_FROM_CURRENCY_ERROR
        return ERROR_FETCHING_VALUE
    
    json_data = response.json(parse_float=Decimal)
    if to_currency not in json_data[from_currency]:
        return INCORRECT_TO_CURRENCY_ERROR
    return json_data[from_currency][to_currency]


def get_rub_to_azn_ratio():
    return get_currency_ratio(
        from_currency="rub",
        to_currency="azn",
    )
        
