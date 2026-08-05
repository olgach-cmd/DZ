import masks


def mask_account_card(num_account_card: str) -> str:
    """
    Принимает на вход строку тип и номер карты или счета в формате
    Visa Platinum 7000792289606361,
    или Maestro 7000792289606361,
    или Счет 73654108430135874305.
    Возвращает строку с замаскированным номером в формате
    Visa Platinum 7000 79** **** 6361 или Счет **4305
    """
    splits_num_account_card = num_account_card.split()
    if splits_num_account_card[0] == "Счет":
        splits_num_account_card[-1] = masks.get_mask_account(splits_num_account_card[-1])
    else:
        splits_num_account_card[-1] = masks.get_mask_card_number(splits_num_account_card[-1])
    return " ".join(splits_num_account_card)


def get_date(date: str) -> str:
    """
    Принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"
     ("11.03.2024").
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
