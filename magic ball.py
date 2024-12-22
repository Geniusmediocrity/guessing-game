from random import *
from termcolor import colored

def start():
    print(colored('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.', 'cyan'))
    total_questions = 0
    while True:
        if total_questions == 0:
            game()
            if again():
                game()
            else:
                print(colored('Возвращайся если возникнут вопросы!', 'light_red'))
                break
        total_questions += 1


def game():
    question = input(colored('Задай вопрос о будущем великому магическому шару\n', 'cyan'))
    answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
                'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
                'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
                'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 
                'Перспективы не очень хорошие', 'Весьма сомнительно']
    index = randint(1, 20)
    print(*answers[index], sep='')


def again():
    trig = input(colored('Хочешь задать еще вопрос великому шару?', 'light_green'))
    if trig.lower() in 'yes' or trig.lower() in 'да':
        return True
    else:
        return False


start()