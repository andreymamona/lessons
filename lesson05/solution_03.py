# Написать функцию, которая используя модуль requests скачивает файл и сохраняет его
# на файловой системе, функция имеет два параметра: ссылка на файл и имя на файловой системе.
# В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
# https://raw.githubusercontent.com/andreymamona/lessons/main/LICENSE
import requests


def download_file(my_url, file_name):
    temp = requests.get(my_url)
    my_file = open(file_name, 'wb')
    my_file.write(temp.content)
#    print(temp.text, '\n', 'Downloaded from:', temp.url, file=my_file)
    my_file.close()


default_address = 'https://raw.githubusercontent.com/andreymamona/lessons/main/LICENSE'
default_file = 'print.txt'
address = input('Input URL or d for default: ')
if address == 'd':
    address = default_address
file = input('Input filename or d for default: ')
if file == 'd':
    file = default_file

download_file(address, file)
