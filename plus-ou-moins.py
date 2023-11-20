from random import *

def AskInt() -> int:
    try:
        () = int()
    except:
        print("Veillez a bien entrer un chiffre")
        continue   
    

while True :
    print("---------------------<3---------------------")
    while True:
        attempts_max= input("Choisissez le nombre de tentatives possibles :")
        AskInt(attempts_max)
    attempts = 1
    score = 0   
    min_nb = (input("Choisissez une borne minimale :"))
    try:
        min_nb = int(min_nb) and min_nb < 100
    except:
        print("La borne minimale doit etre un nombre plus petite que celui de la borne maximale !")
        continue   
    max_nb = (input("Choisissez une borne maximale :"))
    try:
        max_nb = int(max_nb) and min_nb < max_nb and max_nb <=100
    except:
        print("La borne maximale doit etre un nombre plus grand que celui de la borne minimale !")
        continue   
    nb = randint(min_nb,max_nb)

    print("---------------------<3---------------------")
    print("Les bornes sont ",min_nb," et ",max_nb, ".")
    print("Trouvez le nombre en moins de ",attempts_max," tentatives si vous voulez gagner.")

    print("---------------------<3---------------------")
    while score != nb and attempts <= attempts_max:
        remaining_attempts = attempts_max - attempts+1
        print("---------------------<3---------------------")
        print("Il vous reste",remaining_attempts,"tentatives.")
        score = int(input("Choisissez un nombre :"))
        if score < nb:
            print("Plus !")
        elif score > nb:
            print("Moins !")
        else:
            print("---------------------<3---------------------")
            print("Bravo ! Vous avez trouvé le nombre ","en",attempts,"essai(s)")
        attempts += 1

    if attempts>attempts_max and score != nb :
        print("---------------------<3---------------------")
        print("Vous n'avez plus aucune tentative.")
        print("Dommage ! Le bon nombre était : ",nb,".")

        
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ?")
    if reponse.upper() != "Y":
       print("Fin de la partie !")
       break

