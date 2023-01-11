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
    #    city_info = {'name': city_name, 'region': None, 'country': None}
    with open("store/store.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(
                f'Покупатель: {row[0]}| Товары: {row[1]}| Кол-во: {row[2]}|Цена: {row[3]}| Общая стоимость: {int(row[3]) * int(row[2])}')


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
