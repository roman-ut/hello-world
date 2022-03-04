import requests, json
from config import keys
class ConvertExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(currency0: str, currency1: str, quantity: str):
        if currency0 == currency1:
            raise ConvertExeption(f'Не возможно перевести одинаковые валюты: {currency1}')

        try:
            currency0_ = keys[currency0]
        except KeyError:
            raise ConvertExeption(f'Не удалось обработать валюту: {currency0}')

        try:
            currency1_ = keys[currency1]
        except KeyError:
            raise ConvertExeption(f'Не удалось обработать валюту: {currency1}')

        try:
            quantity = float(quantity)
        except ValueError:
            raise ConvertExeption(f'Некорректное значение количества')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currency1_}&tsyms={currency0_}')
        total = json.loads(r.content)[currency0_]

        return total