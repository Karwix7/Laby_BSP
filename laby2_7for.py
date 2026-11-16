liczba = int(input())
i = 1
if liczba == 0:
    print("")
else:
    for n in range(liczba):
        if i == 1:
         print("Python 0")
         i = i + 10
        else:
            n = 2 ** n 
            print("Python "+ str(n))