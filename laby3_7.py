liczba = int(input())
suma = 0
for i in range (liczba):
    wynik = int(input())
    while wynik < 0 or wynik > 100:
        print("Niepoprawny wynik")
        wynik = int(input())
    suma += wynik
print("suma: "+ str(suma))
