#################################################
                # Fonctions
#################################################


# Afficher le résultat nom et âge
def display_the_result(name, age):
    print("Your name is " + name + " and you are " + str(age) + " years old.")
    print("Soon you will be " + str(age + 1) + " years old.")


# Demande du nom à l'utilisateur
def ask_for_the_name():

    name = ""

    while name == "":
        print("Please, enter a name : ")
        name = input()
        print("")

    return name


# Demande de l'âge de l'utilisateur
def ask_for_the_age():

    age = ""

    while age == "":
        print("Please, enter your age : ")
        age = input()
        print("")

    try:
        age == int(age)
    except:
        print("Your age must be a valid number")
        print("")

    return int(age)


# Test sur l'âge
def age_test(age):
    # test de la majorité
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    # commentaire sur l'âge
    if age == 17:
        print("You are almost an adult!")
    elif age == 18:
        print("Congrats!")
    elif age > 60:
        print("You are a senior.")
    elif age < 10 and age > 3:
        print("You are a kid.")
    elif age <= 3:
        print("You are a baby.")
    print("")


def exit_programm():
    print("")
    print("Please press any key to exit the programm.")
    input("")

#################################################
                # Exécution
#################################################

name1 = ask_for_the_name()
age1 = ask_for_the_age()

name2 = ask_for_the_name()
age2 = ask_for_the_age()

display_the_result(name1, age1)
age_test(age1)

display_the_result(name2, age2)
age_test(age2)

exit_programm()