def string_to_integer(string):
    result = ""

    for letter in string:
        result += letter

    return int(result)


def turn_dial(letter, amount, current_dial):
    if letter == "L":

        diff = current_dial - amount

    elif letter == "R":

        diff = current_dial + amount

    return diff % 100


dial = 50
password = 0

with open("input") as f:

    for line in f:
        letter = line[0]
        number = string_to_integer(line[1:])

        dial = turn_dial(letter, number, dial)

        if dial == 0:
            password += 1

print(password)