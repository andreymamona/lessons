# Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки
# с именами участников. Затем каждый играющий по очереди вытягивает бумажку с именем того,
# кому предстоит вручить презент. Ваша программа должна используя список имен участников
# выдать на выходе пары, кто и кому будет дарить, причем сам себе человек не может подарить,
# дубликаты тоже не допустимы.

import random


def secret_santa(*args):
    tmplst = list(args)
    for i in range(len(args)//2):
        a = tmplst[0]
        tmplst.pop(0)
        rnd_int = random.randint(0, len(tmplst) - 1)
        b = tmplst[rnd_int]
        tmplst.pop(rnd_int)
        print(a, b)
    if len(tmplst) > 0:
        print("Без пары:", tmplst[0])


def list_of_coworkers(x):
    my_list = []
    for i in range(x):
        my_list.append(input('Введите имя: '))
    return my_list


# coworkers = ['df', 'fds', 'ere', 'sdfsd', 'rwe', 'ffeet']
number_of_coworkers = int(input('Введите количество сотрудников: '))
coworkers = list_of_coworkers(number_of_coworkers)
secret_santa(*coworkers)
