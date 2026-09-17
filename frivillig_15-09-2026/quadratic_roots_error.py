import sys
import numpy as np

parameter_names = ["a", "b", "c"]
parameter_values = []

try:

    for i in range(1, 4):
        value = float(sys.argv[i])
        parameter_values.append(value)


except IndexError:

    start_index = len(parameter_values)

    for i in range(start_index, 3):
        missing_parameter = float(input(f"Please enter a value for {parameter_names[i]}: "))
        parameter_values.append(missing_parameter)




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


a = parameter_values[0]
b = parameter_values[1]
c = parameter_values[2]

print(quad_roots(a, b, c))