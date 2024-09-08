getal1 = int(input('Wat is de eerste getal?\n'))
getal2 = int(input('Wat is de tweede getal?\n'))

if getal1 > getal2:
    kleiner = getal2
    groter = getal1
elif getal1 < getal2:
    kleiner = getal1
    groter = getal2
else:
    print("De getallen zijn gelijk, dus de uitkomst is 1.")
    exit()

resultaat = groter // kleiner

print(f'Het getal {kleiner} past {resultaat} keer in {groter}')