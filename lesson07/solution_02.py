# Дан список стран и городов каждой страны, где ключи это названия стран, а значения -
# списки городов в этих странах. Написать функцию, которая осуществляет поиск по городу
# и возвращает страну. Оформить в виде программы, которая считывает название города и
# выводит на печать страну.
import csv


def country_search(city_name):
    list_of_cities = []
    with open("cities/city.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            city_info = {'name': city_name, 'region': None, 'country': None}
            if row[3] == city_info['name']:
                city_info['region'] = row[2]
                city_info['country'] = row[1]
                list_of_cities.append(city_info)
                # print(list_of_cities)
                # break
            if row[0] == "END" and list_of_cities is None:
                print('Город не найден')
    with open("cities/region.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for l in range(len(list_of_cities)):
                if row[0] == list_of_cities[l]['region']:
                    list_of_cities[l]['region'] = row[3]
                    # print(city_info)
                    # break
    with open("cities/country.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for l in range(len(list_of_cities)):
                 if row[0] == list_of_cities[l]['country']:
                    list_of_cities[l]['country'] = row[2]
                    # print(city_info)
                    # break
    print(*(f'{value}' for value in list_of_cities if value), sep='\n ', end='.\n')
    #print(list_of_cities)


if __name__ == '__main__':
    input_name = input('Введите название города(на русском): ')
    country_search(input_name)
