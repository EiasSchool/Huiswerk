cijfer = int(input('Voer een cijfer in (tussen 1 en 10):\n'))

if cijfer == 10:
    omschrijving = "uitmuntend"
elif cijfer == 9:
    omschrijving = "zeer goed"
elif cijfer == 8:
    omschrijving = "goed"
elif cijfer == 7:
    omschrijving = "ruim voldoende"
elif cijfer == 6:
    omschrijving = "voldoende"
elif cijfer == 5:
    omschrijving = "bijna voldoende"
elif cijfer == 4:
    omschrijving = "onvoldoende"
elif cijfer == 3:
    omschrijving = "gering"
elif cijfer == 2:
    omschrijving = "slecht"
elif cijfer == 1:
    omschrijving = "zeer slecht"
else:
    print('Dit kan ik niet omzetten!')
    exit()

if cijfer >= 6:
    print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
else:
    print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")