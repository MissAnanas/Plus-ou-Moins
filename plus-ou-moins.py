# Importer "randint" de la base de donnée "random"
from random import randint

# Fonction pour verifier si le joueur a saisit un nombre entier dans une plage donnée
def ask_int(message: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            user_input = int(input(message))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Fonction pour demander au joueur s'il souhaite relancer le jeu (avec ou sans les memes parametres)
def relaunch_game():
    reponse = input("Souhaitez-vous relancer une partie (Y/N) ? ")
    if reponse.upper() == "Y":
        use_same_params = input("Souhaitez-vous utiliser les mêmes paramètres (Y/N) ? ").upper() == "Y"
        return True, use_same_params
    return False, False

# Fonction pour jouer une partie
def play_one_game(min_val, max_val, attempts_max):
    # Generer un nombre aléatoire
    nb = randint(min_val, max_val)
    attempts = 1
    score = 0

    while score != nb and attempts <= attempts_max:
        remaining_attempts = attempts_max - attempts + 1
        print("---------------------♥---------------------")
        print(f"Le numéro se situe entre {min_val} et {max_val}.")
        print("Il vous reste", remaining_attempts, "tentatives.")
        score = ask_int("Choisissez un nombre : ", min_val, max_val)

        if score < nb:
            print("---------------------♥---------------------")
            print("Plus que", score, "!")
        elif score > nb:
            print("---------------------♥---------------------")
            print("Moins que", score, "!")
        else:
            print("---------------------♥---------------------")
            print("Bravo ! Vous avez trouvé le nombre ", "en", attempts, "essai(s).")
            break
        attempts += 1

    if attempts > attempts_max and score != nb:
        print("---------------------♥---------------------")
        print("Vous n'avez plus aucune tentative.")
        print("Dommage ! Le bon nombre était : ", nb, ".")
        print("---------------------♥---------------------")

# Fonction pour lancer le jeu
def launch_game():
    print("---------------------♥---------------------")
    print("Bienvenue sur ce jeu de plus ou moins !")

    # Afficher les regles du jeu
    reponse = input("Souhaitez-vous consulter les règles (Y/N) ? ")
    if reponse.upper() == "Y":
        print("---------------------♥---------------------")
        print("Règles :")
        print("- Le but du jeu est de deviner le chiffre choisi par l'ordinateur. - ")
        print("------> - Définissez le nombre de tentatives que vous aurez,")
        print("------> - Choisissez 2 bornes entre lesquelles un chiffre sera choisi aléatoirement,")
        print("------> - Choisissez un nombre compris entre les bornes,")
        print("------> - Plus ! alors votre nombre est plus petit que celui de l'ordinateur,")
        print("------> - Moins ! alors votre nombre est plus grand que celui de l'ordinateur,")
        print("------> - Attention à bien surveiller vos tentatives restantes !")
        print("---------------------♥---------------------")

    while True:
        # Demander au joueur de definir les parametres du jeu
        attempts_max = ask_int("Choisissez le nombre de tentatives possibles : ", 1, 100)
        min_nb = ask_int("Choisissez une borne minimale : ", 1, 100)
        max_nb = ask_int("Choisissez une borne maximale : ", 1, 100)

        # Verifier si les bornes sont valides
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
            # Joueur une partie avec les parametres definis
            play_one_game(min_nb, max_nb, attempts_max)

            relaunch, use_same_params = relaunch_game()
            if not relaunch:
                print("---------------------♥---------------------")
                print("Fin de la partie !")
                print("---------------------♥---------------------")
                break
            elif not use_same_params:
                break

        if not relaunch:
            break

# Appeler la fonction pour lancer le jeu
launch_game()
