from datetime import datetime


def filter_by_state(processes: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей и опционально значение для ключа state
     (по умолчанию 'EXECUTED').
     Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    result = []
    for process in processes:
        if process["state"] == state:
            result.append(process)

    return result


def sort_by_date(processes: list[dict], reverse: bool = True) -> list[dict]:
    """
    Принимает список словарей и необязательный параметр reverse, задающий порядок сортировки.
    При reverse = True сортирует по убыванию (по умолчанию),
    при reverse = False - сортировка по возрастанию.
    Функция возвращает новый список, отсортированный по дате (date).
    """
    return sorted(processes, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
