def get_mask_card_number(card_number: str | int) -> "str":
    """
    Функция маскировки номера банковской карты
    если номер = 16 символов возвращает маску
    если нет - возвращает ошибку
    """
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        return card_number_str[:4] + " " + card_number_str[5:7] + "** **** " + card_number_str[-4:]
    else:
        return "Некорректный номер карты, ожидается 16 символов"


def get_mask_account(account_number: str | int) -> "str":
    """
    Функция маскировки номера банковского счета
    если номер ≥4 символов возвращает маску
    если нет - возвращает ошибку
    """
    account_number_str = str(account_number)
    if len(account_number_str) >= 4:
        return "**" + account_number_str[-4:]
    else:
        return "Некорректный номер счета, 4 символа и больше"
