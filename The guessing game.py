#Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 
# и просит пользователя угадать это число. 
# Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.


from random import *
from termcolor import colored


def foolproof(check, x, y):
    returner = check.isdigit() and x <= int(check) <= y
    if not returner:
        print(colored('eror 422, please, try again late', 'red') )
        return returner
    else:
        return returner
    


def guessing(x, y):
    more = 'Слишком много, попробуйте еще раз'
    less = 'Слишком мало, попробуйте еще раз'
    win = 'Вы угадали, поздравляем!'
    goodbye = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
    guessed_value = randint(x, y)
    users_value = input(colored('Угадайте загаданное значение:\n', 'cyan'))
    counter = 0
    while foolproof(users_value, x, y):
        if int(users_value) > guessed_value:
            print(colored(more, 'light_blue'))
        elif int(users_value) < guessed_value:
            print(colored(less, 'light_blue'))
        else:
            print(colored(win, 'green'), colored(f'количество попыток:{counter}', 'yellow'), colored(goodbye, 'green'), sep='\n')
            break
        users_value = input()
        counter += 1


def new_game(q):
    if q.lower() in 'да' or q.lower() in 'yes':
        return True
    else:
        print(colored('Пока, надеюсь вы еще вернетсь к нам', 'yellow'))
        return False

    
def values_range():
    print(colored('Укажите диапозон значений', 'light_cyan'))
    min_, max_ = int(input()), int(input())
    if min_ > max_:
        min_, max_ = max_, min_
    guessing(min_, max_)
    

def start():
    games = 0
    print(colored('Добро пожаловать в числовую угадайку!', 'cyan'))
    while True:
        if games == 0:
            values_range()
        elif new_game(input(colored('Хотите продолжить?', 'light_yellow'))):
            values_range()
        else:
            break
        games += 1

        
start()