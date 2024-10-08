# Voornaam: Eias
# Achternaam: Bilal
# Opdracht: Touw trekker

prijzen = {
    3: 1.23,
    4.5: 2.45,
    6.3: 4.10
}

totaal_prijs_all = 0

for diktes in prijzen:
    stukken = int(input(f'Hoeveel stuk {diktes} wilt u?\n'))
    lengte_per_stuk = float(input('Wat is de lengte van elke stuk in meters'))

    totaal_prijs = stukken * lengte_per_stuk * prijzen[diktes]
    totaal_prijs_all += totaal_prijs

    print(f'Diktes: {diktes}mm, Stukken: {stukken}, Lengte: {lengte_per_stuk}m, Total Price {totaal_prijs:.2f}')
    print(f"Totaal prijs voor alle stukken: {totaal_prijs_all:.2f}")
