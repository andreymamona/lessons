# Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
# Добавить конструктор класса и инициализировать атрибуты класса значениями переменных.
# Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

class Dog:
    height = None
    weight = None
    name = None
    age = None

    def __init__(self, height, weight, name, age):
        self.height, self.weight, self.name, self.age = height, weight, name, age

    def jump(self):
        print(f'{self.name} is jumping')

    def run(self):
        print(f'{self.name} is running')

    def bark(self):
        print(f'{self.name} is barking')

    def jump(self):
        print(f'{self.name} is jumping')


if __name__ == "__main__":
    dog = Dog(100, 50, 'Bob', 10)
    dog.jump()
    dog.run()
    dog.bark()

    print(dog.name, dog.age, dog.weight, dog.height)
