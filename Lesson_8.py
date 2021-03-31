#Задача №1
import re

def email_parse(email_address):
    RE_email = re.compile(r'(?P<username>[^&]+)@(?P<domain>[^&]+\.\w+)', re.IGNORECASE) #@\w+.\w+
    if RE_email.match(email_address):
        print(*map(lambda x: x.groupdict(), RE_email.finditer(email_address)))
    else:
        print(f'wrong email: {email_address}')
        raise ValueError

email_parse('someone@geekbrains.ru')

#Задача №3
def type_logger(func):
    def wrapper(*args):
        for msg in args:
            print(f"{func.__name__}({msg}: {type(msg)})")
    return wrapper

@type_logger
def calc_cube(x):
    return x ** 3
a = calc_cube(5)

#Задача №4
def val_checker(func):
    def wrapper(args):
        if args <= 0:
            print(f"wrong val: {args}")
            raise ValueError
        else:
            print(func(args))
    return wrapper

@val_checker
def calc_cube(x):
    return x ** 3

a = calc_cube(-5)