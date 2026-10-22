from RightTriangle import RightTriangle


class Main:

    def main():

        # a)
        triangle1 = RightTriangle(1, 1)
        triangle2 = RightTriangle(3, 4)

        print(triangle1.c)
        print(triangle2.c)

        # b)
        Main.test_RightTriangle()

        # c)
        triangle2.plot_triangle()


    def test_RightTriangle():
        success = False
        msg = "Halllloooo"
        try:
            triangle3 = RightTriangle(1,-1)
        except ValueError:
            success = True
        assert success


if __name__ == "__main__":

    Main.main()