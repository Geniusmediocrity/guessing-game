from random import *
from termcolor import *


list_ = []


def amount():
    return int(input(colored('Введите желаемое количество паролей для генерации:  ', 'light_cyan')))


def length():
    return int(input(colored('Требуемое количество символов в пароле:  ', 'light_cyan')))


def numbers():
    global list_
    question = input(colored('Включать ли в пароль цифры?  ', 'light_yellow'))
    symb = '0123456789'
    if question.lower() in 'yesда':
        list_.extend(symb)


def alpha_lower():
    global list_
    question = input(colored('Включать ли в пароль строчные буквы?  ', 'light_yellow'))
    symb = 'qwertyuiopasdfghjklzxcvbnm'
    if question.lower() in 'yesда':
        list_.extend(symb)


def alpha_upper():
    global list_
    question = input(colored('Включать ли в пароль ПРОПИСНЫЕ буквы?  ', 'light_yellow'))
    symb = 'QWERTYUIOPASDFGHJKLMNBVCXZ'
    if question.lower() in 'yesда':
        list_.extend(symb)


def special_symb():
    global list_
    question = input(colored('Включать ли в пароль специальные символы?  ', 'light_yellow'))
    symb = '!@#$%^&*()_+=-?:;№"[]<>`~'
    if question.lower() in 'yesда':
        list_.extend(symb)


def generator():
    quantity = amount()
    len_ = length()
    numbers(), alpha_lower(), alpha_upper(), special_symb()
    output_list = []
    for i in range(1, quantity + 1):
        for j in range(len_):
            output_list.append(choice(list_))
        print(colored(str(i) + ':   ', 'light_green'),*output_list, sep='')
        output_list = []


generator()