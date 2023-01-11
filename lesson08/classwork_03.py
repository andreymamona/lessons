# Создать новый класс Cat, который имеет все те же атрибуты, что и Dog, только заменить метод bark на meow.


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

class Cat():
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

    def meow(self):
        print(f'{self.name} is meowing')

    def jump(self):
        print(f'{self.name} is jumping')

    def change_name(self, new):
        self.name = new


if __name__ == "__main__":
    dog = Dog(100, 50, 'Bob', 10)
    dog.jump()
    dog.run()
    dog.bark()
    dog.change_name('Jim')

    cat = Cat(50, 10, 'Puss', 3)

    print(dog.name, dog.age, dog.weight, dog.height)
    print(cat.name, cat.age, cat.weight, cat.height)

