from random import *
while True :
    print("---------------------<3---------------------")
    essais_max= int(input("Choisissez le nombre de tentatives possibles :"))
    essais = 1   
    nombre_joueur = 0   
    nombre_min_ordi = int(input("Choisissez une borne minimale :"))
    nombre_max_ordi = int(input("Choisissez une borne maximale :"))
    nombre_ordi = randint(nombre_min_ordi,nombre_max_ordi)

    print("---------------------<3---------------------")
    print("Les bornes sont ",nombre_min_ordi," et ",nombre_max_ordi, ".")
    print("Trouvez le nombre en moins de ",essais_max," tentatives si vous voulez gagner.")

    print("---------------------<3---------------------")
    while nombre_joueur != nombre_ordi and essais <= essais_max:
        essais_restants = essais_max - essais+1
        print("---------------------<3---------------------")
        print("Il vous reste",essais_restants,"tentatives.")
        nombre_joueur = int(input("Choisissez un nombre :"))
        if nombre_joueur < nombre_ordi:
            print("Plus !")
        elif nombre_joueur > nombre_ordi:
            print("Moins !")
        else:
            print("---------------------<3---------------------")
            print("Bravo ! Vous avez trouvé le nombre ","en",essais,"essai(s)")
        essais += 1

    if essais>essais_max and nombre_joueur != nombre_ordi :
        print("---------------------<3---------------------")
        print("Vous n'avez plus aucune tentative.")
        print("Dommage ! Le bon nombre était : ",nombre_ordi,".")

        
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ?")
    if reponse.upper() != "Y":
       print("Fin de la partie !")
       break

