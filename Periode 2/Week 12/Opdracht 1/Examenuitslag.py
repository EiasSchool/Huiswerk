def score(inputText, minValue, maxValue):
    while True:
        try:
            value = int(input(f"{inputText}\n"))
            if minValue <= value <= maxValue:
                return value
            else:
                print(f"Ongeldige invoer moet tussen {minValue} en {maxValue}.")
        except ValueError:
            print("Ongeldige invoer probeer het opnieuw.")


scoreE = score("Voer ScoreE in (0-6):", 0, 6)
scoreP = score("Voer ScoreP in (0-8):", 0, 8)
scoreO = score("Voer ScoreO in (0-5):", 0, 5)
scoreS = score("Voer ScoreS in (0-2):", 0, 2)

totalScore = scoreE + scoreP - scoreO - scoreS

if scoreP == 8 and scoreE > 4 and scoreO == 0 and scoreS == 0:
    resault = "Goed"
elif (scoreS == 0 and totalScore > 7 and totalScore < 13) or (scoreS == 1 and totalScore > 9):
    resault = "Voldoende"
else:
    resault = "Onvoldoende"

print(f"De examenuitslag is: {resault}")