from unittest.mock import patch

import pandas as pd
import pytest

from src.csv_xlsx_parser import parse_csv_file, parse_xlsx_file


@pytest.fixture
def result_ok():
    return [{"id": 1, "amount": 100.5, "date": "2026-01-01"}, {"id": 2, "amount": 200.0, "date": "2026-01-02"}]


@pytest.fixture
def fake_dataframe():
    return pd.DataFrame({"id": [1.0, 2.0], "amount": [100.5, 200.0], "date": ["2026-01-01", "2026-01-02"]})


# тесты parse_csv_file
@patch("src.csv_xlsx_parser.pd.read_csv")
def test_parse_csv_file_ok(mock_read_csv, result_ok, fake_dataframe):
    fake_df = fake_dataframe
    mock_read_csv.return_value = fake_df
    assert parse_csv_file("fake_file.csv", sep=";") == result_ok


@patch("src.csv_xlsx_parser.pd.read_csv")
def test_parse_csv_file_no_file(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError("No such file or directory")
    assert parse_csv_file("no_file.csv", sep=";") == []


@patch("src.csv_xlsx_parser.pd.read_csv")
def test_parse_csv_file_clear(mock_read_csv):
    mock_read_csv.side_effect = pd.errors.EmptyDataError("No columns to parse from file")
    assert parse_csv_file("fake_clear_file.csv", sep=";") == []


# тесты parse_xlsx_file
@patch("src.csv_xlsx_parser.pd.read_excel")
def test_parse_xlsx_file_ok(mock_read_excel, result_ok, fake_dataframe):
    fake_df = fake_dataframe
    mock_read_excel.return_value = fake_df
    assert parse_xlsx_file("fake_file.xlsx") == result_ok


@patch("src.csv_xlsx_parser.pd.read_excel")
def test_parse_xlsx_file_no_file(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError("No such file or directory")
    assert parse_xlsx_file("no_file.xlsx") == []


@patch("src.csv_xlsx_parser.pd.read_excel")
def test_parse_xlsx_file_clear(mock_read_csv):
    mock_read_csv.side_effect = pd.errors.EmptyDataError("No columns to parse from file")
    assert parse_xlsx_file("no_file.xlsx") == []
