import os
from dotenv import load_dotenv
import requests

load_dotenv()

def conversion_currency_in_rub(transaction: dict) -> float:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    """
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(transaction["operationAmount"]["amount"])
    elif currency in ["USD", "EUR"]:
        url = 'https://api.apilayer.com/exchangerates_data/convert'
        params = {
            "to": "RUB",
            "from": currency,
            "amount": transaction["operationAmount"]["amount"]
        }
        api_key = os.getenv('API_KEY')
        headers = {"apikey": api_key}

        result_api = requests.get(url, headers=headers, params=params)


        return float(result_api.json()["result"])
    else:
        raise ValueError("Некорректный код валюты")


