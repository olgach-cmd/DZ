import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании ("description") есть данная строка.
    """
    try:
        res = [transaction for transaction in data if re.search(search, str(transaction.get("description")), flags = re.IGNORECASE)]
        return res
    except AttributeError:
        return[]


def rocess_bank_operations(data:list[dict], categories:list)->dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций ("description"),
    возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
