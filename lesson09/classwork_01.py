# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
# Переопределить магические методы сложения, вычитания, умножения на число.
# Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
# Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
# Создать второй объект класса MyTime, найти разницу с первым, добавить к нему 7 часов и 45 минут,
# вывести на печать результат.
# Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые
# атрибуты: day, month, year. “Исправить” все магические методы для этого класса.
# Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.

class MyTime:
    hours = None
    minutes = None
    seconds = None

    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def conv(self, timestamp):
        hours = timestamp // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        second = timestamp % 60
        return hours, minutes, second

    def __eq__(self, other) -> bool:
        return self.timestamp == other.timestamp

    def __ge__(self, other) -> bool:
        return self.timestamp >= other.timestamp

    def __lt__(self, other) -> bool:
        return self.timestamp < other.timestamp

    def __gt__(self, other) -> bool:
        return self.timestamp > other.timestamp

    def __le__(self, other) -> bool:
        return self.timestamp <= other.timestamp

    def __repr__(self):
        print(f'My time: {self.conv(self.timestamp)}')

    def __str__(self):
        return f'My time: {self.conv(self.timestamp)}'

    def __add__(self, other):
        timestamp = self.timestamp + other.timestamp
        return self.__class__(*self.conv(timestamp))

    def __mul__(self, num):  # multiply
        return self.__class__(*self.conv(self.timestamp * num))  # как заменить на имя текущего класса?

    def __sub__(self, other):
        return self.__class__(*self.conv(self.timestamp - other.timestamp))


class MyDateTime(MyTime):
    day = None
    month = None
    year = None

    def __init__(self, year, month, day, hours, minutes, seconds):
        self.year, self.month, self.day, self.hours, self.minutes, self.seconds = (
            year, month, day, hours, minutes, seconds)
        self.timestamp = (seconds + minutes * 60 + hours * 60 * 60 +
                          day * 24 * 60 * 60 + month * 30 * 24 * 60 * 60 +
                          year * 12 * 30 * 24 * 60 * 60)

    def conv(self, timestamp):
        day = (timestamp % (30 * 24 * 60 * 60)) // (24 * 60 * 60)
        month = (timestamp % (12 * 30 * 24 * 60 * 60)) // (30 * 24 * 60 * 60)
        year = timestamp // (12 * 30 * 24 * 60 * 60)
        hours = (timestamp % (24 * 60 * 60)) // (60 * 60)
        minutes = (timestamp % (60 * 60)) // 60
        second = timestamp % 60
        return year, month, day, hours, minutes, second

    def __repr__(self):
        print(f'My date-time: {self.conv(self.timestamp)}')

    def __str__(self):
        return f'My date-time: {self.conv(self.timestamp)}'

    # def __add__(self, other):
    #     timestamp = self.timestamp + other.timestamp
    #     return MyDateTime(*self.conv(timestamp))

    # def __mul__(self, num):  # multiply
    #     return MyDateTime(*self.conv(self.timestamp * num))  # как заменить на имя текущего класса?

    # def __sub__(self, other):
    #     return MyDateTime(*self.conv(self.timestamp - other.timestamp))


if __name__ == '__main__':
    # time1 = MyTime(12, 12, 12)
    # time2 = MyTime(11, 12, 13)
    # print(time1 + time2)
    # print(time1 * 5)
    # print(time1 - time2)
    # time3 = MyTime(0, 443, 2456)
    # print(time3)
    # time4 = MyTime(1, 2, 3)
    # print(time1 - time4 + MyTime(7, 45, 0))
    date1 = MyDateTime(11, 101, 11, 101, 11, 5)
    date2 = MyDateTime(3, 101, 11, 101, 11, 5)
    print(date1)
    print(date2)
    print(date1 + date2)
    print(date1*2)

