from src.csv_xlsx_parser import parse_csv_file, parse_xlsx_file
from src.processing import sort_by_date
from src.search_and_stats import process_bank_search
from src.utils import list_transactions_from_file
from src.widget import get_date, mask_account_card


def main():
    # сбор данных
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        type_format_file = input("""
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
        """)

        if type_format_file == "1":
            transactions_inform = list_transactions_from_file("data/operations.json")
            break
        elif type_format_file == "2":
            transactions_inform = parse_csv_file("data/transactions.csv")
            break
        elif type_format_file == "3":
            transactions_inform = parse_xlsx_file("data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный номер.")

    while True:
        operation_status = input("""
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """).upper()

        if operation_status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions_inform = [
                transaction for transaction in transactions_inform if transaction.get("state") == operation_status
            ]
            break
        else:
            print(f'Статус операции "{operation_status}" недоступен.')

    while True:
        sort_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if sort_date == "да":
            while True:
                sort_order = input("Отсортировать по возрастанию или по убыванию?\n").lower().split()
                sort_order = sort_order[-1]
                if sort_order in ["возрастанию", "убыванию"]:
                    if sort_order == "возрастанию":
                        reverse = False
                    else:
                        reverse = True
                    transactions_inform = sort_by_date(transactions_inform, reverse=reverse)
                    break
                else:
                    print("Некорректный ввод.\n")
            break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный ввод.\n")

    while True:
        sort_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if sort_rub == "да":
            if type_format_file == "1":
                transactions_inform = [
                    transaction
                    for transaction in transactions_inform
                    if transaction["operationAmount"]["currency"]["code"] == "RUB"
                ]
            else:
                transactions_inform = [
                    transaction for transaction in transactions_inform if transaction.get("currency_code") == "RUB"
                ]
            break
        elif sort_rub == "нет":
            break
        else:
            print("Некорректный ввод.\n")

    while True:
        sort_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if sort_description == "да":
            sort_description = input("Введите слово.\n")
            transactions_inform = process_bank_search(transactions_inform, sort_description)
            break
        elif sort_description == "нет":
            break
        else:
            print("Некорректный ввод.\n")

    if not transactions_inform:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions_inform)}")
        for transaction in transactions_inform:
            if type_format_file == "1":
                transaction_amount = (
                    f"{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}"
                )
            else:
                transaction_amount = f"{transaction["amount"]} {transaction["currency_name"]}"

            if transaction.get("from"):
                print(f"""
{get_date(transaction.get("date"))} {transaction.get("description")}
{mask_account_card(transaction.get("from"))} ->  {mask_account_card(transaction.get("to"))}
Сумма: {transaction_amount}
                """)
            else:
                print(f"""
{get_date(transaction.get("date"))} {transaction.get("description")}
{mask_account_card(transaction.get("to"))}
Сумма: {transaction_amount}
                """)


if __name__ == "__main__":
    main()
