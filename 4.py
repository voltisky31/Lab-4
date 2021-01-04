l = 0
i = 0
while True:
    x = int(input("Podaj liczbę: "))
    if input == 0 or input == "x" or input == "NULL":
        print("Średnia podanych liczb to: ", l/i)
        break
    l += x
    i += 1