import sys
import numpy as np



def quadratic_formula(a, b, root_part=0):
    result = (-b + root_part) / (2*a) # root_part represents plusminus the square root of the discriminant
    return round(result, 2)


def quad_roots(a, b, c):

    discriminant = b**2 - 4*a*c

    if discriminant < 0:

        return "Your equation has no real roots"

    elif discriminant > 0:

        root_part_1 = float(np.sqrt(discriminant))
        root_part_2 = float(-np.sqrt(discriminant))

        return sorted([
            quadratic_formula(a, b, root_part_1),
            quadratic_formula(a, b, root_part_2)
        ])

    else:

        return quadratic_formula(a, b)


a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])


print(quad_roots(a, b, c))