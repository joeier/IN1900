s = 0
M = 3

# I for-løkken har jeg gjort følgende endringer:
#   1. Erklære tellevariabelen som k istedenfor i slik at k faktisk eksisterer
#   2. Forandret parameterne i range-funksjonen sånn at tellingen begynner med 1 og går til og med 3
#   3. La til parenteser i formelen slik at Python regner i riktig rekkefølge
for k in range(1, M+1):
    s += 1 / ((2*k)**2)

print(s)