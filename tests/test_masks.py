import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def number_not_digit():
    return "dlfkgjlsdkskfsdl"


@pytest.fixture
def few_number():
    return "78"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_not_digit(number_not_digit):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(number_not_digit)


def test_get_mask_card_number_len(few_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(few_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("6831982476737658", "**7658"),
        ("8247", "**8247"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_not_digit(number_not_digit):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(number_not_digit)


def test_get_mask_account_len(few_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(few_number)
