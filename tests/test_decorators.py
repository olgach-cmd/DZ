from pathlib import Path

import pytest
from src.decorators import log

# функции для проверки декороторов
@log()
def division(a, b):
    return a / b

filename = "log.txt"
@log(filename)
def summ(a, b):
    return a + b

# тесты
def test_log_to_file():
    summ(2, 3)
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    assert "function summ start" in content
    assert "function summ ok" in content

def test_log_to_file_err():
    with pytest.raises(Exception):
        summ("2", 3)
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    assert "function summ start" in content
    assert "function summ error: TypeError. Inputs: ('2', 3)" in content

def test_log_to_console(capsys):
    division(2, 3)
    captured = capsys.readouterr()
    assert "function division start" in captured.out
    assert "function division ok" in captured.out

def test_log_to_console_err(capsys):
    with pytest.raises(Exception):
        division(5, 0)
    captured = capsys.readouterr()
    assert "function division start" in captured.out
    assert "function division error: ZeroDivisionError. Inputs: (5, 0)" in captured.out


