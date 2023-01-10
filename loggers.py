from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        call_time= datetime.now().strftime('%d-%m-%Y  %H:%M:%S')
        func_name = old_function.__name__
        res = old_function(*args, **kwargs)
        with open ('main.log', 'a', encoding='utf-8') as log:
            log.write(f"""{func_name}
Время вызова функции - {call_time}
Аргументы функции - {args, kwargs}
Значение функции - {res}\n\n""")
        return res
    return new_function

def logger_v2(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            call_time= datetime.now().strftime('%d-%m-%Y  %H:%M:%S')
            func_name = old_function.__name__
            res = old_function(*args, **kwargs)
            with open (path, 'a', encoding='utf-8') as log:
                log.write(f"""{func_name}
Время вызова функции - {call_time}
Аргументы функции - {args, kwargs}
Значение функции - {res}\n\n""")
            return res
        return new_function
    return logger
