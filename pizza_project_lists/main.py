import random


def display(list):
    if len(list) == 0:
        print("There is no Pizza here... :(")
        return

    print("Pizza (" + str(len(list)) + ")")
    for i in list:
        print("----- Pizza : " + i + " -----")

    print()
    print("First entry : " + list[0])
    print("Last entry : " + list[-1])
    print()


def exit_programm():
    print("")
    print("Please press any key to exit the programm.")
    input("")


def add_user_pizza(list):
    new_entry = input("Veuillez entrer un nom de pizza à ajouter à la base de données : ")
    
    # while pizza_exists(new_entry, list):                                                  
    if new_entry.lower() in list:         # une manière plus simple pour éviter l'usage d'un appel à une fonction et la création d'une autre boucle
        print("This pizza already exist, please enter a new pizza.")
        new_entry = input("Veuillez entrer un nom de pizza à ajouter à la base de données : ")
    
    list.append(new_entry)
    print("Pizza added")
    print()


# def pizza_exists(str, list):              # voir commentaire dans la fonction add_user_pizza()
#     for i in list:
#         if i == str:
#             return True
#     return False


pizzas = ["4 cheeses", "vegetarian", "hawai", "calzone", "four seasons"]
# empty_collection = []

display(pizzas)
add_user_pizza(pizzas)
display(pizzas)

exit_programm()
