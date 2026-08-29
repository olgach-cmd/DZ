from datetime import datetime
from functools import wraps

def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper (*args, **kwargs):
            # функция для записи логов
            def write_log(message):
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f"{datetime.now()} {message} \n")
                else:
                    print(f"{datetime.now()} {message} \n")

            write_log(f"func {func.__name__} start")
            try:
                result = func(*args, **kwargs)
                write_log(f"func {func.__name__} ok")
                return result


            except Exception as e:
                write_log(f"func {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper
    return decorator

