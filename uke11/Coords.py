import numpy as np


class Coords:

    def __init__(self, x: float, y: float, z: float):
        self._x = round(x, 2)
        self._y = round(y, 2)
        self._z = round(z, 2)

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __len__(self):
        return 3

    def __abs__(self):
        val = np.sqrt(self._x**2 + self._y**2 + self._z**2)
        return f"{val:.2f}"

    def __add__(self, other: Coords):
        x_new = self._x + other._x
        y_new = self._y + other._y
        z_new = self._z + other._z
        return Coords(x_new, y_new, z_new)

    def __sub__(self, other: Coords):
        x_new = self._x - other._x
        y_new = self._y - other._y
        z_new = self._z - other._z
        return Coords(x_new, y_new, z_new)


print("a)")
sqrt3 = np.sqrt(3)
close = Coords(1/sqrt3, 1/sqrt3, 1/sqrt3)
far = Coords(3/sqrt3, 15/sqrt3, 21/sqrt3)
print(close)
print(far)

print("\nb)")
print(f"The class represents coordinates in {len(close)} dimensions")
print(f"The distance from the centre to the point close is {abs(close)}")
print(f"The distance from the centre to the point far is {abs(far)}")

print("\nc)")
further = close + far
print(f"The coordinates further are at {further}")
distance = abs(far - close)
print(f"The distance from far to close is {distance}")
centre = further - further
print(f"The coordinates at the centre are {centre}")