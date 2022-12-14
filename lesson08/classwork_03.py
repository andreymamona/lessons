# Создать новый класс Cat, который имеет все те же атрибуты, что и Dog, только заменить метод bark на meow.

from library.dog import Dog
from library.cat import Cat

if __name__ == "__main__":
    dog = Dog(100, 50, 'Bob', 10)
    dog.jump()
    dog.run()
    dog.bark()
    dog.change_name('Jim')

    cat = Cat(50, 10, 'Puss', 3)

    print(dog.name, dog.age, dog.weight, dog.height)
    print(cat.name, cat.age, cat.weight, cat.height)

