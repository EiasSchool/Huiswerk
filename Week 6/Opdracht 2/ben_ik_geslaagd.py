# Voornaam: Eias
# Achternaam: Bilal
# Opdracht: Verificatie


def diploma():
    print('Welkom bij het diploma-verificatieprogramma.')

    nederlands = float(input('Voer je eindcijfer in voor Nederlands: '))
    engels = float(input('Voer je eindcijfer in voor Engels: '))
    rekenen = float(input('Voer je eindcijfer in voor Rekenen: '))
    devskills = float(input('Voer je cijfer in voor DevSkills: '))

    dimensies = ["politiek-juridisch", "economisch", "maatschappelijk-sociaal", "vitaal burgerschap"]
    burgerschap = {}
    for dimensie in dimensies:
        antwoord = input(f'Heb je de dimensie {dimensie} behaald? (ja/nee): ').strip().lower()
        burgerschap[dimensie] = antwoord == 'ja'

    keuzedeel_1 = float(input('Voer je cijfer in voor Keuzedeel 1: '))
    keuzedeel_2 = float(input('Voer je cijfer in voor Keuzedeel 2: '))

    stage_1 = input('Heb je de oriënterende stage gehaald? (ja/nee): ').strip().lower() == 'ja'
    stage_2 = input('Heb je de eindstage gehaald? (ja/nee): ').strip().lower() == 'ja'
    totaal_uren = int(input('Voer het totaal aantal geregistreerde stage-uren in: '))

    examen_software = float(input('Voer je cijfer in voor \'Realiseren Software\': '))
    examen_team = float(input('Voer je cijfer in voor \'Werken in een Ontwikkelteam\': '))

    resultaten = {
        'Nederlands': nederlands >= 5.5,
        'Engels': engels >= 5.5,
        'Rekenen': rekenen >= 5.5,
        'DevSkills': devskills >= 5.5,
        'Burgerschap': all(burgerschap.values()),
        "Keuzedeel 1": keuzedeel_1 >= 5.5,
        "Keuzedeel 2": keuzedeel_2 >= 5.5,
        "Stages": stage_1 and stage_2 and totaal_uren > 1400,
        "Realiseren Software": examen_software > 5,
        "Werken in een Ontwikkelteam": examen_team > 5

    }

    alles_behaald = all(resultaten.values())

    print('\nResultatenoverzicht:')
    for vak, behaald in resultaten.items():
        print(f'{vak}: {'Voldoende' if behaald else 'Onvoldoende'}')

    print('\nEindresultaat:')
    if alles_behaald:
        print("Gefeliciteerd! Je komt in aanmerking voor je diploma!")
    else:
                print("Helaas, je komt niet in aanmerking voor je diploma.")
diploma()