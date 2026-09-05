import json

import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(funcName)s: %(levelname)s: %(message)s')
logger.addHandler(file_handler)
file_handler.setFormatter(file_formatter)


def list_transactions_from_file(file_path: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    logger.info(f"Начало чтение из файла {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        logger.info(f"Данные о транзакциях успешно сохранены")
        return data
    except (json.decoder.JSONDecodeError, FileNotFoundError) as ex:
        logger.exception(f"Произошла ошибка {ex}")
        return []
