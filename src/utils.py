import json

def list_transactions_from_file(file_path: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except json.decoder.JSONDecodeError:
        return []

