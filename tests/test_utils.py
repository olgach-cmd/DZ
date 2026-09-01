from src.utils import list_transactions_from_file


# Тесты list_transactions_from_file
def test_list_transactions_from_file(list_transactions):
    assert list_transactions_from_file(r"data\operations.json") == list_transactions


def test_list_transactions_from_file_clear():
    assert list_transactions_from_file(r"data\operations_clear.json") == []


def test_list_transactions_from_file_no_json():
    assert list_transactions_from_file(r"data\operations_no_json.json") == []


def test_list_transactions_from_file_no_file():
    assert list_transactions_from_file(r"data\operations_.json") == []
