from typing import Any, Generator


def filter_by_currency(transactions: list[dict], code: str) -> Generator[dict, None, None]:
    """
    Генераторная функция, принимает на вход список словарей, представляющих транзакции,
    и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    (например, USD).
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, None, None]:
    """
    Генераторная функция, принимает на вход список словарей, представляющих транзакции,
    и возвращает описание каждой операции по очереди (например, "Перевод организации")
    """
    for transaction in transactions:
        yield transaction["description"]
#
# def card_number_generator():
#     """
#     Генераторная функция, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
#     Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
#     """


