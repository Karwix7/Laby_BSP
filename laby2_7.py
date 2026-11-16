liczba = int(input())
i = 1
n = 1
if liczba == 0:
    print("")
else:
    while i <= liczba:
        if i == 1:
         print("Python 0")
         i = i + 1
        else:
            n = 2 ** i 
            print("Python "+ str(n))
            i = i + 1
