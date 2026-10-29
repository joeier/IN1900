import matplotlib.pyplot as plt
import numpy as np


class Diff:

    def __init__(self, f: function):
        self._f = f

    def diff1(self, x: float, h: float):
        f = self._f

        return (f(x+h) - f(x)) / (h)

    def diff2(self, x: float, h: float):
        f = self._f

        return (f(x+h) - f(x-h)) / (2*h)

    def diff3(self, x: float, h: float):
        f = self._f

        return (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)) / (12*h)


def read_h():
    try:
        return float(input("Skriv inn en verdi for h: "))
    except:
        print("\nVerdien du skriver inn må være et tall!")
        return read_h()


diffs = Diff(lambda x : np.sin(np.pi * 2 * x))
exact_diff = lambda x : np.pi * 2 * np.cos(np.pi * 2 * x)

h = read_h()

datapoints = 1000
x_values = np.linspace(-1, 1, datapoints)
exact_values, diff1_values, diff2_values, diff3_values = [np.zeros(datapoints) for i in range(4)]

for i in range(datapoints):
    exact_values[i] = exact_diff(x_values[i])
    diff1_values[i] = diffs.diff1(x_values[i], h)
    diff2_values[i] = diffs.diff2(x_values[i], h)
    diff3_values[i] = diffs.diff3(x_values[i], h)

plt.plot(x_values, exact_values, label="Nøyaktig deriverte")
plt.plot(x_values, diff1_values, label="diff1")
plt.plot(x_values, diff2_values, label="diff2")
plt.plot(x_values, diff3_values, label="diff3")

plt.grid()
plt.legend()
plt.show()
