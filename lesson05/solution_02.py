# Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки
# с именами участников. Затем каждый играющий по очереди вытягивает бумажку с именем того,
# кому предстоит вручить презент. Ваша программа должна используя список имен участников
# выдать на выходе пары, кто и кому будет дарить, причем сам себе человек не может подарить,
# дубликаты тоже не допустимы.

import random


def secret_santa(*args):
    people = list(args)
    random.shuffle(people)
    for index in range(len(people)):
    # Special case when we match the last person in list to the first
        if index == len(people) - 1:
            print(f"{people[index]} - {people[0]}")
        else:
            print(f"{people[index]} - {people[index + 1]}")


# def list_of_coworkers(x):
#     my_list = []
#     for i in range(x):
#         my_list.append(input('Введите имя: '))
#     return my_list


coworkers = ['df', 'fds', 'ere', 'sdfsd', 'rwe', 'ffeet']
# number_of_coworkers = int(input('Введите количество сотрудников: '))
# coworkers = list_of_coworkers(number_of_coworkers)
secret_santa(*coworkers)

