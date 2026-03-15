# 1-Le Pris Mystère

import random

print(" Bienvenue dans le jeu du Pris mystère ! ")
print(" Le but du jeu est deviner un nombre entre 1 et 100. ")

prix = random.randint(1, 100)
tentative = 0 
trouve = False

while not trouve:
    guess = int(input(" Votre proposition : "))
    tentative += 1  
    if guess < prix:
        print(" C'est plus ")
    elif guess > prix:
        print(" C'est moins ")
    else:
        print(f"Bravo vous avez trouvé le prix mystère", prix,  "au bout de", tentative, "tentatives")
        trouve = True