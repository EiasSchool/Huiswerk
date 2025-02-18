band_kost = float(input('Hoeveel kost een nieuwe band?\n'))
arbeid_per_band = float(input('Hoeveel kost de arbeid per band?\n'))
lampje_kost = float(input('Hoeveel kost een nieuw lampje?\n'))
lampje_vervangen_kost = float(input('Hoeveel kost het om een lampje te vervangen?\n'))

totaal_banden = 2 * (band_kost + arbeid_per_band)
totaal_lampjes = 2 * (lampje_kost + lampje_vervangen_kost)

totaal = totaal_banden + totaal_lampjes
print(f"De totale kosten voor het vervangen van de banden en lampjes is: € {totaal:.2f}")