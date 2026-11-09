liczbaa = float(input())
operator = str(input())
liczbab = float(input())
if (operator == "+"):
    print(liczbaa + liczbab)

if (operator == "-"):
    print(liczbaa - liczbab)
if (liczbaa == 0 or liczbab == 0):
    print("Nie można dzielić przez zero")
else:
     print(liczbaa / liczbab)

if (operator == "*"):
    print(liczbaa * liczbab)