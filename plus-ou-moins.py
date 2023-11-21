from random import *

def AskInt(message: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            user_input = int(input(message))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

def relaunch_game():
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ? ")
    if reponse.upper() == "Y":
        use_same_params = input("Souhaitez-vous utiliser les mêmes paramètres (Y/N) ? ").upper() == "Y"
        return True, use_same_params
    return False, False

print("---------------------<3---------------------")
print("Bienvenue sur ce jeu de plus ou moins !")
reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
if reponse.upper() == "Y":
    print("---------------------<3---------------------")
    print("Règles :")
    print("- Le but du jeu est de deviner le chiffre choisi par l'ordinateur. - ")
    print("------> - Définissez le nombre de tentatives que vous aurez,")
    print("------> - Choisissez 2 bornes entre lesquelles un chiffre sera choisi aléatoirement,")
    print("------> - Choisissez un nombre compris entre les bornes,")
    print("------> - Plus ! alors votre nombre est plus petit que celui de l'ordinateur,")
    print("------> - Moins ! alors votre nombre est plus grand que celui de l'ordinateur,")
    print("------> - Attention à bien surveiller vos tentatives restantes !")
    print("---------------------<3---------------------")
        
while True:
    print("---------------------<3---------------------")
    attempts_max = AskInt("Choisissez le nombre de tentatives possibles : ", 1, 100)
    
    attempts = 1
    score = 0

    min_nb = AskInt("Choisissez une borne minimale : ", 1, 100)
    max_nb = AskInt("Choisissez une borne maximale : ", 1, 100)

    if min_nb >= max_nb:
        print("La borne minimale doit être strictement inférieure à la borne maximale. Veuillez recommencer.")
        continue

    try:
        assert min_nb < 100
        assert min_nb < max_nb <= 100
    except AssertionError:
        print("Les bornes ne sont pas valides. Veuillez recommencer.")
        continue

    while True:
        nb = randint(min_nb, max_nb)

        print("---------------------<3---------------------")
        print("Les bornes sont ", min_nb, " et ", max_nb, ".")
        print("Trouvez le nombre en moins de ", attempts_max, " tentatives si vous voulez gagner.")

        while score != nb and attempts <= attempts_max:
            remaining_attempts = attempts_max - attempts + 1
            print("---------------------<3---------------------")
            print("Il vous reste", remaining_attempts, "tentatives.")
            score = AskInt("Choisissez un nombre : ", 1, 100)

            if score < nb:
                print("Plus !")
            elif score > nb:
                print("Moins !")
            else:
                print("---------------------<3---------------------")
                print("Bravo ! Vous avez trouvé le nombre ", "en", attempts, "essai(s)")
            attempts += 1

        if attempts > attempts_max and score != nb:
            print("---------------------<3---------------------")
            print("Vous n'avez plus aucune tentative.")
            print("Dommage ! Le bon nombre était : ", nb, ".")
            print("---------------------<3---------------------")

        relaunch, use_same_params = relaunch_game()
        if not relaunch:
            print("---------------------<3---------------------")
            print("Fin de la partie !")
            print("---------------------<3---------------------")
            break
        elif use_same_params:
            attempts = 1
            score = 0
        else:
            break
    if not relaunch:
        break