#Utilisation des matchs cases
boisson = "eau"
match boisson:
    case "eau":
        print("J'adore l'eau, dans 20/30 ans il n'y en aura plus.")
    case "coca":
        print("Je n'apprécie guère le coca.")
    case "orangina":
        print("en sah l'orangina c'est surcote")
    case _:
        print("Je ne connais pas cette boisson")