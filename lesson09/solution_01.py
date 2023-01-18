# Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
# Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
# методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки,
# методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение
# площади и периметра). При потребности создавать все необходимые методы не описанные в задании.
# Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
import math
import random


class Point:
    x = None
    y = None

    def __init__(self, a, b):
        if a == 'x' and b == 'y':
            self.x = random.randint(-50, 50)
            self.y = random.randint(-50, 50)
        else:
            self.x, self.y = a, b

    def __str__(self):
        return f'Point: {self.x}, {self.y}'


class Figure:
    perimetr = None
    ploshcha = None

    def __str__(self):
        return f'Perimetr: {self.perimetr},Ploshcha: {self.ploshcha}'

    def dlina(self, a1=None, a2=None):
        dl = math.sqrt((a1.x - a2.x) ** 2 + (a1.y - a2.y) ** 2)
        return dl


class Circle(Figure):
    center = None
    radius = None

    def __init__(self, center, radius):
        self.center, self.radius = center, radius
        self.find_perimetr()
        self.find_ploshcha()

    def find_perimetr(self):
        self.perimetr = 2 * 3.1416 * self.radius

    def find_ploshcha(self):
        self.ploshcha = 3, 1416 * (self.radius ** 2)


class Triangle(Figure):
    a1 = None
    a2 = None
    a3 = None

    def __init__(self, a1, a2, a3):
        self.a1, self.a2, self.a3 = a1, a2, a3
        self.find_perimetr()
        self.find_ploshcha()
        print(self.a1, self.a2, self.a3)

    def find_perimetr(self):
        self.perimetr = self.dlina(self.a1, self.a2) + self.dlina(self.a1, self.a3) + self.dlina(self.a2, self.a3)
        print(self.perimetr)

    def find_ploshcha(self):
        self.ploshcha = 0.5 * abs((self.a1.x - self.a3.x) * (self.a2.y - self.a3.y) -
                                  (self.a2.x - self.a3.x) * (self.a1.y - self.a3.y))
        print(self.ploshcha)


class Square(Figure):
    ...


if __name__ == '__main__':
    a1 = Point('x', 'y')
    a2 = Point('x', 'y')
    a3 = Point('x', 'y')
    print(a1, a2, a3)
    cir = Circle(a1, 7)
    triang = Triangle(a1, a2, a3)
    print(cir)
    print(triang)
