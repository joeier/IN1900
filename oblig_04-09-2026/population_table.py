import math



n = 12
interval = [0, 48]
step = (interval[1] - interval[0]) / n
t = []
N = []


# Bakterievekstfunksjonen i lambda-format. Dette gjorde jeg bare fordi jeg ville teste ut den måten å skrive funksjoner på :)
bacteriaFunction = lambda t : 50000 / (1 + 9*math.e**(-0.2*t))



for i in range(interval[0], interval[1] + 1, int(step)):
    t.append(i)
    N.append(bacteriaFunction(i))


# Her bygger jeg tabellen
print("Time    |Bakterieantall")        # Printer tabelloverskrifter
print("________|_______________")       # Printer en fin skillelinje mellom overskrifter og tabelldata
for i in range(len(t)):                 # Jeg iterer gjennom en liste over indeksene til t-lista istedenfor elementene. På den måten kan jeg enkelt hente elementer fra både t og N
    print(f"{t[i]:8}|{N[i]:10.2f}")     # Her skrives tabelldataene ut. Fordi tallene er av ulik lengde formaterer jeg dem slik at den ene kolonnen aldri blir lenger enn 8 og den andre 10. På den måten ser tabellen fin ut
print("--------|---------------")       # Printer en fin skillelinje mellom tabelldataene og slutten på tabellen