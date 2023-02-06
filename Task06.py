# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

import random

rand_number = random.randint(0, 100)

# print(rand_number)


def guess_number(random_n, count=1):
    guess = int(input('Введите число: '))
    if guess == random_n:
        print('Ждите повестки в Хогвартс.')
        return -1
    else:
        if guess < random_n and count != 10:
            print(f'Загаданное число больше введенного. Осталось попыток: {10-count}')
            return guess_number(random_n, count+1)
        elif guess > random_n and count != 10:
            print(f'Загаданное число меньше введенного. Осталось попыток: {10-count}')
            return guess_number(random_n, count+1)


guess_number(rand_number)
