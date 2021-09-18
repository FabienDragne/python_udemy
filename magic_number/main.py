####################################################
                # import
####################################################

import random

####################################################
                # global variable
####################################################

MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4

lives = NB_LIVES


####################################################
                # function
####################################################

# Je demande d'entrer un nombre au joueur
def ask_number(min_nb, max_nb):
    print("What is the magic number between " + str(MIN_NUMBER) + " and " + str(MAX_NUMBER) + "?")
    user_guess_int = 0                          
    while user_guess_int == 0:                                      # Tant que ma variable est à 0
        user_guess_str = input()
        try:                                                        # je compare que mes deux user_guess se valent
            user_guess_int = int(user_guess_str)
        except:                                                     # si ce n'est pas le cas je renvoie une erreur
            print("ERROR: You must enter a number. Please retry.")  # la boucle reprend...
        else:                                                       
            if MIN_NUMBER < user_guess_int > MAX_NUMBER:
                print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
                user_guess_int = 0
    return user_guess_int


def player_winning_or_not(nb):
    global lives
    if nb > MAGIC_NUMBER:
        print("The magic number is lower!")
        print("")
        lives -= 1
    elif nb < MAGIC_NUMBER:
        print("The magic number is greater!")
        print("")
        lives -= 1
    else:
        print("Congratulation ! You won !")


def play():
        winning = False
        while not winning:
            player_answer = ask_number(MIN_NUMBER, MAX_NUMBER)
            player_winning_or_not(player_answer)
            if MAGIC_NUMBER == player_answer:
                winning = True        

def exit_programm():
    print("")
    print("Please press any key to exit the programm.")
    input("")


####################################################
                # execution
####################################################

play()
exit_programm()

####################################################
                # 
####################################################
####################################################
                # 
####################################################
####################################################
                # 
####################################################