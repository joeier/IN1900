import numpy as np


def extract_data(filename):

    temp_list = []

    with open(filename) as f:

        f.readline()

        for line in f:

            for temp in line.split():

                temp_list.append(float(temp))

    return temp_list


def make_weather_data(data):

    avg = float(np.mean(data))

    dataset = {
        "Gjennomsnittlig": round(avg, 1),
        "Minste": np.min(data),
        "Største": np.max(data)
        }

    return dataset


def print_data(dataset):
    print("Temperature data from ")


oct_1945 = make_weather_data(extract_data("temp_oct_1945.txt"))
oct_2014 = make_weather_data(extract_data("temp_oct_2014.txt"))

print("Temperaturdata fra oktober 1945")
for key, value in oct_1945.items():
    print(f"{key}: {value} grader celsius")

print("\n")

print("Temperaturdata fra oktober 2014")
for key, value in oct_2014.items():
    print(f"{key}: {value} grader celsius")