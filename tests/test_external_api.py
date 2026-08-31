import os
from unittest.mock import patch

import pytest

from src.external_api import conversion_currency_in_rub


@patch("requests.get")
def test_conversion_currency_in_rub_usd(mosk_api_result):
    mosk_api_result.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1788201184, "rate": 86.299251},
        "date": "2026-08-31",
        "result": 709498.073194,
    }
    assert (
        conversion_currency_in_rub(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 709498.073194
    )
    mosk_api_result.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": os.getenv("API_KEY")},
        params={"to": "RUB", "from": "USD", "amount": "8221.37"},
    )


def test_conversion_currency_in_rub_rub():
    assert (
        conversion_currency_in_rub(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )


def test_conversion_currency_in_rub_other_currency():
    with pytest.raises(ValueError) as exc_info:
        conversion_currency_in_rub(
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "SZL", "code": "SZL"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
        )
