# Создать программу, которая импортирует класс из предыдущей задачи, создает объект и
# при инициализации устанавливает марку Mercedes, модель E500, год выпуска 2000. Далее
# “разгоняет” машину до 100 км/ч и выводит скорость на экран.

from solution_01 import Car

if __name__ == '__main__':
    my_car = Car('Mercedes', 'E500', '2000')
    my_car.target_speed(100, True)