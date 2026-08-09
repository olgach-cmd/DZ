def filter_by_state(processes: list[dict], state: str='EXECUTED') -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state
     (по умолчанию 'EXECUTED').
     Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    result = []
    for process in processes:
        if process['state'] == state:
            result.append(process)

    return result


def sort_by_date():
    pass