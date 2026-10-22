import numpy as np
import matplotlib.pyplot as plt
import sys

from Diff import Diff


class Main:

    def main(args=0.1):

        diffs = Diff(lambda x : np.sin(np.pi * 2 * x))
        exact_diff = lambda x : np.pi * 2 * np.cos(np.pi * 2 * x)

        h = float(args[1])

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


if __name__ == "__main__":

    Main.main(sys.argv)