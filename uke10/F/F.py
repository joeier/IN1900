import numpy as np


class F:

    def __init__(self, m: float, n: float):

        self._m = m
        self._n = n


    def __call__(self, x: float):

        return np.sin(self._n * x) * np.cos(self._m * x)


    def xy_lists(self, length: int):

        x = np.linspace(0, 2 * np.pi, length)
        y = np.zeros(length)

        for i in range(length):

            y[i] = self.__call__(x[i])

        return (x, y)