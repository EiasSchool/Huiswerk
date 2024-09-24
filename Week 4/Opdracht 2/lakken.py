import math

hoogte_deur = float(input("Voer de hoogte van de deur in meters in (bijv. 2.0): "))
breedte_deur = float(input("Voer de breedte van de deur in meters in (bijv. 0.8): "))
aantal_deuren = int(input("Voer het aantal deuren in (bijv. 13): "))
oppervlakte_per_blik = float(input("Voer het aantal vierkante meters dat één blik verf dekt (bijv. 6.0): "))
prijs_per_blik = float(input("Voer de prijs van één blik verf in (bijv. 23.45): "))
oppervlakte_per_vel_schuurpapier = float(input("Voer de oppervlakte in m² die één vel schuurpapier kan opschuren (bijv. 1.5): "))
prijs_per_vel_schuurpapier = float(input("Voer de prijs van één vel schuurpapier in (bijv. 0.47): "))

oppervlakte_per_deur = hoogte_deur * breedte_deur
totale_oppervlakte = 2 * oppervlakte_per_deur * aantal_deuren

aantal_blikken = math.ceil(totale_oppervlakte / oppervlakte_per_blik)

totale_kosten_verf = aantal_blikken * prijs_per_blik

aantal_vellen_schuurpapier = math.ceil(totale_oppervlakte / oppervlakte_per_vel_schuurpapier)

totale_kosten_schuurpapier = aantal_vellen_schuurpapier * prijs_per_vel_schuurpapier

print(f"Totale oppervlakte om te verven: {totale_oppervlakte:.2f} vierkante meter")
print(f"Benodigde aantal verfblikken: {aantal_blikken}")
print(f"Totale kosten voor verf: €{totale_kosten_verf:.2f}")
print(f"Benodigde aantal vellen schuurpapier: {aantal_vellen_schuurpapier}")
print(f"Totale kosten voor schuurpapier: €{totale_kosten_schuurpapier:.2f}")
