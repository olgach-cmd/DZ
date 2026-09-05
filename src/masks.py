import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(funcName)s: %(levelname)s: %(message)s')
logger.addHandler(file_handler)
file_handler.setFormatter(file_formatter)



def get_mask_card_number(card_number: str | int) -> "str":
    """
    Функция маскировки номера банковской карты
    если номер = 16 цифр возвращает маску
    если нет - возвращает ошибку
    """
    logger.info(f"Начало маскировки номера карты с номером {card_number}")
    card_number_str = str(card_number)
    if not card_number_str.isdigit():
        logger.error(f"Номер карты содержит нецифровые символы")
        raise ValueError("номер карты должен состоять из цифр")
    elif len(card_number_str) == 16:
        logger.info(f"")
        mask = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
        logger.info(f"Номер карты успешно замаскирован {mask}")
        return mask
    else:
        logger.error(f"Некорректная длина номера карты {len(card_number_str)}, ожидается 16 цифр")
        raise ValueError("Некорректный номер карты, ожидается 16 цифр")


def get_mask_account(account_number: str | int) -> "str":
    """
    Функция маскировки номера банковского счета
    если номер ≥4 цифр возвращает маску
    если нет - возвращает ошибку
    """
    logger.info(f"Начало маскировки номера счета с номером {account_number}")
    account_number_str = str(account_number)
    if not account_number_str.isdigit():
        logger.error(f"Номер  содержит нецифровые символы")
        raise ValueError("номер счета должен состоять из цифр")
    elif len(account_number_str) >= 4:
        mask = "**" + account_number_str[-4:]
        logger.info(f"Номер счета успешно замаскирован {mask}")
        return mask
    else:
        logger.error(f"Некорректная длина номера счета {len(account_number_str)}, ожидается 4 цифры и больше")
        raise ValueError("Некорректный номер счета, ожидается 4 цифры и больше")
