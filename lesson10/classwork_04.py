# Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + N**M.
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyIter:
    n = None
    m = None
    step = 1
    summ = 0

    def __init__(self, n, m):
        self.n, self.m = n, m

    def __iter__(self):
        return self

    def __next__(self):
        if self.step <= self.m + 1:
            if self.step == self.m + 1:
                self.step += 1
                return f'Sum: {self.summ}'
            else:
                tmp = self.n ** self.step
                self.summ += tmp
                self.step += 1
                return f'N**{self.step-1} = {tmp}'
        else:
            raise StopIteration


if __name__ == '__main__':
    my_array = MyIter(2, 10)
    while True:
        try:
            logger.info(f'num {next(my_array)}')
        except StopIteration:
            break
