x = 0
y = 0
z = 0
while True:
    y = x
    x = int(input("Podaj liczbę: "))
    z += x
    if x == y:
        print("Suma podanych liczb to: ", z)
        break