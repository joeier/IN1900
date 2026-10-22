import numpy as np
import matplotlib.pyplot as plt


class RightTriangle:

    def __init__(self, a: float, b: float):

        if a < 0 or b < 0:

            raise ValueError("Either a or b has a negative value - a triangle length should be strictly positive")


        self._a = a
        self._b = b
        self.c = np.sqrt(a**2 + b**2) # Dropper understrek foran c fordi den ifølge oppgaven skal hentes ut utenfor klassen


    def plot_triangle(self):

        x = np.zeros(4)
        y = np.zeros(4)

        x[1] = self._a
        y[2] = self._b

        plt.plot(x, y)
        plt.axis("equal")
        plt.grid()
        plt.show()