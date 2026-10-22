import matplotlib.pyplot as plt

from F import F


class Main:

    def main():

        u = F(1, 2)
        v = F(3, 4)

        u_lists = u.xy_lists(1000)
        v_lists = v.xy_lists(1000)

        plt.plot(u_lists[0], u_lists[1], label="u")
        plt.plot(v_lists[0], v_lists[1], label="v")
        plt.grid()
        plt.legend()
        plt.show()


if __name__ == "__main__":

    Main.main()