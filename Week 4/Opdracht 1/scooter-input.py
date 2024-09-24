band_kost = float(input('Hoeveel kost een nieuwe band? (Standaard prijs is € 57,79)\n') or 57.79)
arbeid_per_band = float(input('Hoeveel kost de arbeid per band? (Standaard prijs is € 15,00)\n') or 15.00)
lampje_kost = float(input('Hoeveel kost een nieuw lampje? (Standaard prijs is € 1,45)\n') or 1.45)
lampje_vervangen_kost = float(input('Hoeveel kost het om een lampje te vervangen? (Standaard prijs is € 2,10)\n') or 2.10)

totaal_banden = 2 * (band_kost + arbeid_per_band)
totaal_lampjes = 2 * (lampje_kost + lampje_vervangen_kost)

totaal = totaal_banden + totaal_lampjes
print(f"De totale kosten voor het vervangen van de banden en lampjes is: € {totaal:.2f}")