def get_mask_card_number(card_number: str | int) -> "str | int":
    """
    Функция маскировки номера банковской карты
    если номер = 16 символов возвращает маску
    если нет - возвращает номер
    """
    card_number_str = str(card_number)
    if len(card_number_str) == 16:
        return card_number_str[:4] + " " + card_number_str[5:7] + "** **** " + card_number_str[-4:]
    else:
        return card_number


def get_mask_account(account_number: str | int) -> "str | int":
    """
    Функция маскировки номера банковского счета
    если номер ≥4 символов возвращает маску
    если нет - возвращает номер
    """
    account_number_str = str(account_number)
    if len(account_number_str) >= 4:
        return "**" + account_number_str[-4:]
    else:
        return account_number
