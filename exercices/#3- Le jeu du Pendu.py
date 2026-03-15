#3- Le jeu du Pendu

mot_mystère = "python"
mot_visible = ["*"] * len(mot_mystère)
nb_vies = 10

while True:
    print("Mot : ", "".join(mot_visible))
    print("Nombre de vies : ", nb_vies)

    lettre = input("Entrez une lettre : ")

    if lettre in mot_mystère:
        for i, char in enumerate(mot_mystère):
            if char == lettre:
                mot_visible[i] = lettre
                # mot_visible = mot_visible[:i] + lettre + mot_visible[i+1:]
    else:
        nb_vies -= 1
        
    if mot_mystère == "".join(mot_visible):
        print("Félicitations, vous avez gagné !")
        break
    elif nb_vies == 0:
        print("Désolé, vous avez perdu. Le mot était : ", mot_mystère)
        
