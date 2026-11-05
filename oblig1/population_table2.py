import math



n = 12
interval = [0, 48]
step = (interval[1] - interval[0]) / n
tN1 = [[], []]
tN2 = []


# Bakterievekstfunksjonen i lambda-format. Dette gjorde jeg bare fordi jeg ville teste ut den måten å skrive funksjoner på :)
bacteriaFunction = lambda t : 50000 / (1 + 9*math.e**(-0.2*t))



for i in range(interval[0], interval[1] + 1, int(step)):
    tN1[0].append(i)
    tN1[1].append(round(bacteriaFunction(i)))
    tN2.append([i, round(bacteriaFunction(i))])


# På grunn av ulik indeksering mellom tN1 og tN2, har jeg delt opp tabellbyggingen i to funksjoner - den ene bygger tabellen med tN1 og den andre med tN2
def print_tN1():
    print("Time    |Bakterieantall")
    print("________|_______________")
    for i in range(len(tN1[0])):
        print(f"{tN1[0][i]:8}|{tN1[1][i]:10}")
    print("--------|---------------")



def print_tN2():
    print("Time    |Bakterieantall")
    print("________|_______________")
    for i in range(len(tN2)):
        print(f"{tN2[i][0]:8}|{tN2[i][1]:10}")
    print("--------|---------------")


# Siste linje kan du endre på avhengig av om du vil bygge tabellen med tN1 eller tN2. På den måten printer programmet kun 1 tabell (for oversiktens skyld)
print_tN2()