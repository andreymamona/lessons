# Создать генератор и/или итератор простой геометрической прогрессии.

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def gen_func(q, m, n):  # q-коэф.прогрессии, m-кол-во шагов прогрессии, n1-первый эл-т
    for i in range(0, m+1):
        if i != 0:
            n = n*q
            yield n
        else:
            yield n, q


if __name__ == '__main__':

    q = int(input('input q: '))
    m = int(input('input m: '))
    n = int(input('input n: '))
    my_gen = gen_func(q, m, n)
    for i in range(m+1):
        logger.info(f'Step: {i}, num {next(my_gen)}')
    # while True:
    #     try:
    #         print(next(my_gen))
    #     except StopIteration:
    #         break


