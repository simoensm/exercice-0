# exercice-0
Purpose = transform several phrases into words
📝 Description

Ce programme parcourt une phrase caractère par caractère et affiche chaque caractère sur une nouvelle ligne.
Il réinitialise ensuite la variable utilisée pour construire le mot, ce qui entraîne l'affichage isolé de chaque caractère.
À la fin de l'exécution, le programme affiche le message "fini !".

💻 Code
phrases = "J'aime les vaches et les poussins"
mot=""
for item in phrases:
    mot+=item
    print (mot)
    
    mot=""
print("fini !")

🔍 Fonctionnement

phrases contient une chaîne de caractères.

La boucle for parcourt cette chaîne un caractère à la fois.

mot += item ajoute ce caractère dans la variable mot.

Le programme affiche mot, qui contient alors uniquement le caractère courant.

mot = "" réinitialise la variable, empêchant la construction d’un véritable mot.

À la fin, "fini !" est imprimé pour indiquer la fin du programme.
