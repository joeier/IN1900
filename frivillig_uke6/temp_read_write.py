import numpy as np


def extract_data(filename):

    temp_data = {
        "filename": filename,
        "temps": []
        }

    with open(filename) as f:

        f.readline()

        for line in f:

            for temp in line.split():

                temp_data["temps"].append(float(temp))

    return temp_data


def make_weather_data(data):

    avg = float(np.mean(data["temps"]))

    data["Average"] = round(avg, 1)
    data["Lowest"] = np.min(data["temps"])
    data["Highest"] = np.max(data["temps"])

    return data


def print_data(dataset):

    time = dataset["filename"].split("_")

    month = time[1]
    year = time[2].split(".")[0]

    print(f"Temperature for {month} {year}")

    for key, value in list(dataset.items())[2:]:
        
        print(f"{key}: {value} degrees celsius")

    print("\n")


oct_1945 = make_weather_data(extract_data("temp_oct_1945.txt"))
oct_2014 = make_weather_data(extract_data("temp_oct_2014.txt"))

print_data(oct_1945)
print_data(oct_2014)