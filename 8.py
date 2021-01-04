i = 1
kwota = 0
odl = 333
while i <= 12:
    kwota += odl
    kwota = kwota * 1.08
    print(i, "miesiąc oszczędności: ", kwota)
    i += 1