####################################################
                # import
####################################################


import random

####################################################
                # global variables
####################################################


MIN_NUMBER = 1
MAX_NUMBER = 10


####################################################
                # functions
####################################################


def chose_nb_of_question():
    return int(input("How many compute do you want to do? "))


def exit():
    print("")
    input("press enter to exit...")


def ask_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    o = random.randint(0, 1)

    if o == 1:
        answer = input("What's the result of " + str(a) + " + " + str(b) + "? ")
        if a + b == int(answer):
            return True
        return False
    else:
        answer = input("What's the result of " + str(a) + " * " + str(b) + "? ")
        if a * b == int(answer):
            return True
        return False

def play():
    nb_of_points = 0
    nb_of_questions = chose_nb_of_question()
    for i in range (1, nb_of_questions + 1):
        print()
        print("Question " + str(i) + " out of " + str(nb_of_questions) + " : ")
        if ask_question():
            nb_of_points += 1
    print()
    print("You finished with " + str(nb_of_points) + " points out of " + str(nb_of_questions) + " !")

    if nb_of_points == nb_of_questions:
        print("Perfect score ! Congratulations !")
    elif nb_of_points == 0:
        print("You really need to improve your maths.")
    elif nb_of_points < (int(nb_of_questions/2)):
        print("You can do better.")
    elif nb_of_points > (int(nb_of_questions/2)):
        print("Good.")




####################################################
                # execute
####################################################

play()
exit()
