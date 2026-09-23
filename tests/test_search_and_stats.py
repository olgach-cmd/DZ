import pytest

from src.search_and_stats import process_bank_operations, process_bank_search


@pytest.fixture
def transactions():
    return [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def categories():
    return ["Открытие вклада", "Перевод со счета на счет", "Перевод организации"]


# тесты process_bank_search
def test_process_bank_search(transactions):
    assert process_bank_search(transactions, "перевод") == transactions
    assert process_bank_search(transactions, "Организации") == [transactions[1]]


@pytest.mark.parametrize(
    "transactions_no_list_dic, expected",
    [([], []), ([1, 2, 3], []), ({1: "1", 2: "2", 3: "3"}, [])],
)
def test_process_bank_search_no_list_dic(transactions_no_list_dic, expected):
    assert process_bank_search(transactions_no_list_dic, "перевод") == expected


@pytest.mark.parametrize(
    "no_str_search, expected",
    [([], []), ([1, 2, 3], []), ({1: "1", 2: "2", 3: "3"}, [])],
)
def test_process_bank_search_no_str_search(transactions, no_str_search, expected):
    assert process_bank_search(transactions, no_str_search) == expected


# тесты process_bank_operations
def test_process_bank_operations(list_transactions, categories):
    assert process_bank_operations(list_transactions, categories) == {
        "Открытие вклада": 10,
        "Перевод со счета на счет": 15,
        "Перевод организации": 40,
    }
