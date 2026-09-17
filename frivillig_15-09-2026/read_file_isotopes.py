oxygen_mass = 0.0


with open("oxygen.txt") as f:
    f.readline()


    for line in f:
        values = line.split()
        m = float(values[1])
        w = float(values[2])

        oxygen_mass += m*w


print(f"{oxygen_mass:.4f} g/mol")