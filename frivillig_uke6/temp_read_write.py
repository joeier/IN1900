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

    templist = data["temps"]

    avg = float(np.mean(templist))

    data["Average"] = round(avg, 1)
    data["Lowest"] = np.min(templist)
    data["Highest"] = np.max(templist)

    return data


def print_data(dataset):

    file_subnames = dataset["filename"].split("_")

    month = file_subnames[1]
    year = file_subnames[2].split(".")[0] # file_subnames[2] is "{year}.txt", therefore split(".")

    print(f"Temperature for {month} {year}")

    for key, value in list(dataset.items())[2:]:
        
        print(f"{key}: {value} degrees celsius")

    print("\n")


def write_formatting(filename, dataset1, dataset2):

    with open(filename, "w") as f:

        


# a)
oct_1945 = make_weather_data(extract_data("temp_oct_1945.txt"))
oct_2014 = make_weather_data(extract_data("temp_oct_2014.txt"))

print_data(oct_1945)
print_data(oct_2014)


# b)
