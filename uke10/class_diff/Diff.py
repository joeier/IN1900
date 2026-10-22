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