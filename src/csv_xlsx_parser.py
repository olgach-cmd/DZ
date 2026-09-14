import pandas as pd
import json

def parse_csv_file(file_path: str, sep: str = ";") -> list[dict]:
    """
    Функция принимает на вход путь до csv-файла и разделитель (по умолчанию разделитель ";") и возвращает список словарей с транзакциями.
    Если файл пустой или не найден, функция возвращает пустой список.
    """
    try:
        transactions_df = pd.read_csv(file_path,sep=sep, encoding='utf-8')
        transactions_df['id'] = transactions_df['id'].astype('Int64')
        transactions_dic = transactions_df.to_dict(orient="records")

        return transactions_dic
    except (FileNotFoundError,pd.errors.EmptyDataError) as ex:
        return []


    # return json.loads(transactions_df.to_json(orient='records', force_ascii=False))
    return transactions_dic


def parse_xlsx_file(file_path: str):
    """
    Функция принимает на вход путь до xlsx-файла и возвращает список словарей с транзакциями.
    Если файл пустой или не найден, функция возвращает пустой список.
    """
    try:
        transactions_df = pd.read_excel(file_path)
        transactions_df['id'] = transactions_df['id'].astype('Int64')
        transactions_dic = transactions_df.to_dict(orient="records")
        return transactions_dic
    except (FileNotFoundError,pd.errors.EmptyDataError) as ex:
        return []

