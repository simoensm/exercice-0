phrases = "J'aime les vaches et les poussins"
mot = ""

for item in phrases:
    if item != " ":        # On construit un mot tant qu’on ne rencontre pas un espace
        mot += item
    else:
        print(mot)
        mot = ""           # On réinitialise pour le mot suivant

print(mot)  # On affiche le dernier mot
print("fini !")