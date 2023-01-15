# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
# Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп
# (сброс скорости на 0), отображение скорости, задний ход (изменение знака скорости).

class Car:

    brand = None
    model = None
    year_prod = None
    direction = True # True for forward, False for backward
    speed = 0
    max_forward_speed = 200
    max_backward_speed = 40

    def __init__(self, brand, model, year_prod):
        self.brand, self.model, self.year_prod = brand, model, year_prod
        print(f'Your car is ', self.brand, self.model, ', ', self.year_prod, 'year production', sep=' ')

    def speed_up(self):
        if self.direction:
            if self.speed >= self.max_forward_speed:
                print(f'Max f.speed is 200')
                self.display_speed()
            else:
                self.speed += 5
                self.display_speed()
        else:
            if self.speed >= self.max_backward_speed:
                print(f'Max b.speed is 40')
                self.display_speed()
            else:
                self.speed += 5
                self.display_speed()

    def speed_down(self):
        if self.speed > 0:
            self.speed -= 5
            self.display_speed()
        else:
            print('You are stopped')

    def stop(self):
        while self.speed > 0:
            self.speed -= 5
        self.display_speed()

    def display_speed(self):
        if self.direction:
            tmp_dir = 'forward'
        else:
            tmp_dir = 'backward'
        print(f'Speed is ', self.speed, ', direction is ', tmp_dir, sep='')

    def revers_move(self):
        self.stop()
        self.direction = not self.direction
        self.display_speed()

    def target_speed(self, tar_speed, tar_dir):
        if tar_speed > self.max_forward_speed and tar_dir:
            tar_speed = self.max_forward_speed
        elif tar_speed > self.max_backward_speed and not tar_dir:
            tar_speed = self.max_backward_speed
        if tar_dir != self.direction:
            self.revers_move()
        if tar_speed > self.speed:
            while tar_speed > self.speed:
                self.speed_up()
        elif tar_speed == self.speed:
            self.display_speed()
        else:
            while tar_speed < self.speed:
                self.speed_down()

    def change_definition(self, brand_0, model_0, year_prod_0):
        self.brand = brand_0
        self.model = model_0
        self.year_prod = year_prod_0
        print(f'Your car is ', self.brand, self.model, ', ', self.year_prod, 'year production', sep=' ')


if __name__ == "__main__":
    my_car = Car()
    new_brand = input("Brand: ")
    new_model = input('Model: ')
    new_year_prod = input('year of production: ')
    my_car.change_definition(new_brand, new_model, new_year_prod)
    new_dir_tmp = input('Choose your direction (f/b): ')
    if new_dir_tmp == 'f':
        new_dir = True
    elif new_dir_tmp == 'b':
        new_dir = False
    else:
        new_dir = True
        print('Wrong choice! You will drive forward!')
    new_speed = abs(int(input('Choose your speed: ')))
    my_car.target_speed(new_speed, new_dir)


