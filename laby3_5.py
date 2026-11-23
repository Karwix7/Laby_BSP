liczba = int(input())
wynik = 0
warto = 0

while liczba != 0:
    wynik += liczba
    warto += 1
    liczba = int(input())
else:
    print("suma: " +str(wynik))
    print("suma wartości: " +str(warto))