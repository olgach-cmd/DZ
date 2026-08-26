from typing import Generator


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


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генераторная функция, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    if len(str(start)) > 16 or start <= 0 or len(str(stop)) > 16 or stop < start:
        raise ValueError(
            "Неверно задан диапазон значений. Сгенерировать номер карт можно в диапазоне от 1 до 9999999999999999"
        )
    for i in range(start, stop + 1):
        str_i = str(i)
        num_cart = "0" * (16 - len(str_i)) + str_i
        yield f"{num_cart[0:4]} {num_cart[4:8]} {num_cart[8:12]} {num_cart[12:16]}"
