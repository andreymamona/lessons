# Создать общий класс Animal, содержащий все общие методы классов Dog и Cat.
# Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы,
# которые имеются у родительского класса. Создать объект каждого класса и вызвать все его методы.

from library.animal import Animal

class Cat(Animal):
    def meow(self):
        print(f'{self.name} is meowing')

class Dog(Animal):
    def bark(self):
        print(f'{self.name} is barking')


if __name__ == "__main__":
    dog = Dog(100, 50, 'Bob', 10)
    dog.bark()
    dog.change_name('Jim')

    cat = Cat(50, 10, 'Puss', 3)
    cat.meow()

    print(dog.name, dog.age, dog.weight, dog.height)
    print(cat.name, cat.age, cat.weight, cat.height)
