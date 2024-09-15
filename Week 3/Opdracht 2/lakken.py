import math

hoogte_deur = 2.0
breedte_deur = 0.8  
aantal_deuren = 13  
oppervlakte_per_blik = 6.0 
prijs_per_blik = 23.45  
oppervlakte_per_vel_schuurpapier = 1.5
prijs_per_vel_schuurpapier = 0.47 

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
