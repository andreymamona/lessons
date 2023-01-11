# Добавить в класс Dog метод change_name. Метод принимает на вход новое имя
# и меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
# Вызвать метод change_name. Вывести имя.


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

    def change_name(self, new):
        self.name = new


if __name__ == "__main__":
    dog = Dog(100, 50, 'Bob', 10)

    dog.jump()
    dog.run()
    dog.bark()
    dog.change_name(input('input name:'))

    print(dog.name, dog.age, dog.weight, dog.height)
