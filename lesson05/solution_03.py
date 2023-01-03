# Написать функцию, которая используя модуль requests скачивает файл и сохраняет его
# на файловой системе, функция имеет два параметра: ссылка на файл и имя на файловой системе.
# В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
# https://raw.githubusercontent.com/andreymamona/lessons/main/LICENSE

import requests

default_address = 'https://raw.githubusercontent.com/andreymamona/lessons/main/LICENSE'



test = requests.get('https://raw.githubusercontent.com/andreymamona/lessons/main/LICENSE')
print(test.text)

my_file = open('print.txt', 'w')
print(test.text, '\n', 'Downloaded from:', test.url, file=my_file )
my_file.close()
