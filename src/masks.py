def get_mask_card_number(card_number: str | int) -> "str":
    """
    Функция маскировки номера банковской карты
    если номер = 16 цифр возвращает маску
    если нет - возвращает ошибку
    """
    card_number_str = str(card_number)
    if not card_number_str.isdigit():
        raise ValueError("номер карты должен состоять из цифр")
    elif len(card_number_str) == 16:
        return card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    else:
        raise ValueError("Некорректный номер карты, ожидается 16 цифр")


def get_mask_account(account_number: str | int) -> "str":
    """
    Функция маскировки номера банковского счета
    если номер ≥4 цифр возвращает маску
    если нет - возвращает ошибку
    """
    account_number_str = str(account_number)
    if not account_number_str.isdigit():
        raise ValueError("номер счета должен состоять из цифр")
    elif len(account_number_str) >= 4:
        return "**" + account_number_str[-4:]
    else:
        raise ValueError("Некорректный номер счета, ожидается 4 цифры и больше")
