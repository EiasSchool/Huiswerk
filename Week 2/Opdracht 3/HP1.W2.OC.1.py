geld = 10000
rentepercentage = 2.8

rente = rentepercentage / 100

bedrag_5_jaar = geld * (1 + rente) ** 5
bedrag_15_jaar = geld * (1 + rente) ** 15

print(f"Na 5 jaar heb je ongeveer {bedrag_5_jaar:.2f} euro.")
print(f"Na 15 jaar heb je ongeveer {bedrag_15_jaar:.2f} euro.")