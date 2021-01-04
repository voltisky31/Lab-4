l = 0
i = 0
while True:
    x = int(input("Podaj liczbę: "))
    i += 1
    if l >= 100:
        print("Przekroczyłeś sumę 100")
        break
    if l/i >= 66:
        print("Przekroczyłeś średnią 66")
        break
    l += x