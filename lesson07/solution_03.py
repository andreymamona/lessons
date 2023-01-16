# Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина.
# Каждая строка входного файла представляет собой запись вида Покупатель, Товар, Количество, Стоимость,
# где Покупатель - имя покупателя (строка без пробелов), товар - название товара (строка без пробелов),
# количество - количество приобретенных единиц товара.
# a. Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте
# общее количество приобретенных им товаров и их стоимость.
# b. Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее
# количество приобретенных и их стоимость.

import csv


def buyers_list():
    with open("store/store.csv", "r") as file:
        reader = csv.reader(file)
        buyers = {}
        for row in reader:
            if row[0] in buyers.keys():
                 buyers[row[0]][0] += int(row[2])  # summary quantity
                 buyers[row[0]][1] += int(row[2])*int(row[3])  # sum.cost
            else:
                buyers[row[0]] = [0, 0]
                buyers[row[0]][0] = int(row[2])
                buyers[row[0]][1] = int(row[2])*int(row[3])
    for key, value in buyers.items():
        print(f'Покупатель: {key}| Кол-во товаров: {buyers[key][0]}| Стоимость: {buyers[key][1]}')


def goods_list():
    with open("store/store.csv", "r") as file:
        reader = csv.reader(file)
        goods = {}
        for row in reader:
            if row[1] in goods.keys():
                 goods[row[1]][0] = int(row[2]) + int(goods[row[1]][0])
            else:
                goods[row[1]] = [0, 0, 0]
                goods[row[1]][0] = int(row[2])
                goods[row[1]][1] = int(row[3])
    for key, value in goods.items():
        goods[key][2] = int(goods[key][0]) * int(goods[key][1])
        print(f'Товар: {key}| Кол-во: {goods[key][0]}| Цена: {goods[key][1]}| Стоимость: {goods[key][2]}')


if __name__ == '__main__':
    input_name = input('Что показать (a/b): ')
    if input_name == 'a':
        buyers_list()
    elif input_name == 'b':
        goods_list()
    else:
        print('Unknown input!')
