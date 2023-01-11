# Дан список стран и городов каждой страны, где ключи это названия стран, а значения -
# списки городов в этих странах. Написать функцию, которая осуществляет поиск по городу
# и возвращает страну. Оформить в виде программы, которая считывает название города и
# выводит на печать страну.
import csv


def country_search(city_name):
    city_info = {'name': city_name, 'region': None, 'country': None}
    with open("cities/city.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == city_info['name']:
                city_info['region'] = row[2]
                city_info['country'] = row[1]
                # print(city_info)
                # break
            if row[0] == "END":
                print('Город не найден')
    with open("cities/region.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == city_info['region']:
                city_info['region'] = row[3]
                # print(city_info)
                break
    with open("cities/country.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == city_info['country']:
                city_info['country'] = row[2]
                print(city_info)
                break


if __name__ == '__main__':
    input_name = input('Введите название города(на русском): ')
    country_search(input_name)
