
from math import sqrt


def solution(area):

    if area < 1 or area > 1000000:
        print('Area must be between 1 and 1000000')
    if sqrt(area).is_integer():
        return [area]
    biggest = int(sqrt(area)) ** 2
    return [biggest] + solution(area - biggest)


my_area = int(input('Area:'))
print(solution(my_area))
