# Afficher dans la console
# print()

####################################################
                # variable / constant
####################################################

# ma_variable = 1
# ma_seconde_variable = "deux"
# ma_troisième_variable = 1.75
# MA_CONSTANTE = 3

# Les constantes n'existe pas en python, néanmoins par convention,
# on écrit le nom des variables dont on ne veut pas voir changer les valeurs en majuscules

# Pour affecter une variable globale depuis un bloc de code, 
# on "redéclare" d'abord notre variable à l'intérieur de ce dernier précédé du mot "global",
# puis on peut intéragir normalement avec au sein du bloc

# exemple:

# c = 0 # global variable

# def add():
#     global c
#     c = c + 2 # increment by 2
#     print("Inside add():", c)

# add()
# print("In main:", c)

# https://www.programiz.com/python-programming/global-keyword

####################################################
                        # print
####################################################

print("Bienvenue dans ce fichier cheat sheet dédié à Python!")
print("ver. 1")
print()

# je peux print des str et des int, 
# mais dans le cas d'un int, il devra être seul ou cast préalablement en str
# on ne peut concaténer un int avec un str autrement

# On peut également print sur plusieurs ligne simplement

print("""
 , __           _                  
/|/  \         | |                 
 |___/     _|_ | |     __   _  _   
 |    |   | |  |/ \   /  \_/ |/ |  
 |     \_/|/|_/|   |_/\__/   |  |_/
         /|                        
         \|  

""")

####################################################
                        # input()
####################################################

# input("Veuillez entrer une valeur : ")

# arrête le déroulement du programme le temps que la réponse soit entrée par l'utilisateur

# test_input = input("Veuillez entrer une valeur qui sera sauvegardé dans la variable test_input ")
# print("La valeur entrée est : " + test_input)

# input renvoit toujours un string


####################################################
                    # commentaire
####################################################

# commentaire sur une seule ligne

""" Commentaire
    sur
    plusieurs
    lignes """

####################################################
                    # type()
####################################################

# afficher le type d'une variable

# test_type_string = "texte d'exemple"
# test_type_int = 17

# print(type(test_type_int))
# print(type(test_type_string))

####################################################
                # Conversion (cast)
####################################################

# convertir un string vers un int

# variable_string_test = "33"
# calcul_test = int(variable_string_test) + 14

# convertir un integer en string

# variable_int_test = 147
# print(str(variable_int_test))

# convertir un string en float
# variable_string_test2 = "1.75"
# my_first_float = float(variable_string_test2)

####################################################
            # try / except / finally / else
####################################################

# Pour prévoir le comportement du programme en cas d'erreur

# exemple :
# je déclare un string que je vais tenter d'utiliser dans une opération arithmétique

# print("Entrez une valeur de test")
# valeur_de_test = input()

# try:
#     nouvelle_valeur = int(valeur_de_test) + 1               # tentative
# except:
#     print("L'opération ne peut fonctionner")                # action en cas d'échec
#     print("vous devez rentrer un nombre.")
# finally:                                                       
#     print("L'opération n'a rencontré aucun problème")         # action si aucun échec
# else:                               
#     print("")                                                 # action en cas d'echec


# https://careerkarma.com/blog/python-try-except/

####################################################
            # while loop / boucle while
####################################################

# boucle while qui va içi s'effectuer 5 fois

# n = 0                         # On déclare une variable

# while n < 5:                  # On donne la condition avec laquelle la boucle prendra fin
#     print("ligne " + str(n))
#     n += 1

# On peut utiliser "not" dans les conditions d'une boucle while

# password = ""

# while not password == "1234":
#     password = input("What is the password? ")

# print("password is correct, you have access to the account.")

####################################################
            # for loop / boucle for
####################################################

# la boucle for s'exécutera pour un nombre de tour donné

# for i in range(0, 4):       # for (déclaration de la boucle) i (par convention, i pour index) in range(0, 4) de 0 à 3
#     print(i)

####################################################
            # fonction / function
####################################################

# la fonction retourne une information
# par convention on sépare deux définitions de fonctions par deux sauts de ligne

# portée des variables:
# une variable déclarée dans une fonction n'existe qu'à l'intérieur de cette dernière
# une fois sortie de la fonction, la variable est supprimmée
# on peut donc réutiliser des noms de variables extérieur à la fonction
# pour faire appel à une variable en dehors de la fonction, on ajout le terme "global" avant l'appel de cette dernière

# exemple :
# global name = ""
# changera directement la valeur de name en dehors de la fonction en lui affectant une string vide

# def ask_for_the_name():                         # def pour définir la fonction
#     name = ""
#     while name == "":
#         print("Please, enter a name : ")
#         name = input()
#     return name                                 # return pour indiquer la variable à retourner

# paramètre(s) et paramètre(s) optionnel(s)

# fonction avec paramètres, à l'appel de la fonction on appelle les paramètres des arguments
# def print_firstname_and_name(firstname = "John", name = "Doe"): # içi j'ai affecté des valeurs par défaut aux paramètres
#     print(firstname + " " + name)

# si jamais l'un des paramètres n'était pas donné, la fonction imprimmerait la valeur par défaut
# les paramètres optionnels doivent toujours se situer en fin de liste

# print_firstname_and_name()
# print_firstname_and_name("Fabien", "Dragne")
# print_firstname_and_name("Fabien")

# je ne peux appeler ma fonction avec un argument vide suivi d'arguments
# si je veux un équivalent, il me faudra prévoir au sein de la fonction un comportement
# pour un argument "absent", par exemple en mettant "None"

# https://stackoverflow.com/questions/28569551/is-it-correct-to-pass-none-to-a-parameter
# https://realpython.com/python-optional-arguments/#using-python-optional-arguments-with-default-values


####################################################
                # conditions
####################################################

# age = 7

# if age >= 18:                       # si age est plus grand ou égale à 18 alors...
#     print("You are an adult")
# elif age <= 3:                      # sinon si age est plus petit ou égale à 3 alors...
#     print("You are a baby")         # ("elif" pour "else if")
# else:                               # sinon...
#     print("Your are a minor")

# Je peux mettre autant de elif que nécessaire

# Même si l'indentation peut sembler indiquer le contraire, if, elif et else dans cet exemple
# font parti du même bloc de code, si les conditions de if sont validées, alors les instructions
# suivantes dans elif et else ne seront pas utilisées

# Si l'on voulait que les trois conditions sont vérifiées indépendament, alors il faudrait remplacer
# elif et else par if

####################################################
                # comparaison
####################################################

# == equality

# > plus grand que
# >= plus grand ou égale que

# < plus petit que
# <= plus petit ou égale que

# bool : True/False la majuscule est nécessaire

# and : et
# or : ou

# exemple

# age = 17
#                                             # comme on compare deux fois la variable age, on peut l'écrire:
# if age < 18 and age >= 10:                  # if 10 <= age < 18:
#     print("You are a teenager.")
# elif age < 10 or age >= 18:                 # Un simple else aurait pu suffir, mais c'est pour l'exemple
#     print("You are not a teenager.")

####################################################
                # import
####################################################

# pour importer des "modules" (basiquement des bibliothèques):
# exemple:

# import turtle               # j'importe mon module

# t = turtle.Turtle()         # j'initialise une variable t, nécessaire au module

# # ...                       les instructions pour déplacer la tortue

# turtle.done()               # empêche la fenêtre graphique de se fermer

# Quelques modules à importer:

# import random                  # donne accès à random.randint (par exemple) pour définir une valeur aléatoire

####################################################
                # increment / decrement
####################################################

# l'utilisation de l'incrémentation avec ++ n'existe pas en python
# on utilise simplement le +=

# a = 1
# a += 1              # donc 2

####################################################
            # Collections / Tuples / List
####################################################

    # tuples
    ########################

# Les tuples sont des tableaux immuable (immutable, ne pouvant être changé une fois déclaré)
# de par leur nature, ils sont moins gourmand en mémoire que les "lists" présentées après
# déclaration avec des paranthèses

# new_tuples_test_str = ("Mon premier élément", "Mon second élément", "Mon troisième élément", "Mon quatrième élément")
# new_tuples_test_int = (15, 27, 3, 98, 55)
# new_tuples_test_mixt = ("Mon premier élément", 13, "Mon second élément", 77, 88)
# new_tuples_of_tuples = (new_tuples_test_str, new_tuples_test_str, new_tuples_test_mixt)

# persons = ("Brian", "Bob", "Alice", "Jean")

# print(len(persons))                # affiche la longueur du tableau persons, içi 4
# print(persons[0])                  # imprimme le contenu du premier élément du tableau persons, içi "Brian"
# print(persons[-1])                 # je peux également parcourir mon tableau en sens inverse


# print(new_tuples_of_tuples)               # renvoie tous les éléments du tableau
# print(len())

    # list
    ########################

# déclaration avec des crochets

# persons = ["Brian", "Bob", "Alice", "Jean"]         # déclaration de la list
# new_person = "David"                                # déclaration d'une variable que je veux rajouter ensuite à ma list
# persons.append(new_person)                          # ajout de l'élément "new person" à la fin de mon tableau
# persons[0] = "Steeven"                              # içi je change le premier élément de ma list (Brian par Steeven)


####################################################
#                                                  #
#                                                  #
#               Fonctions diverses                 #
#                                                  #
#                                                  #
####################################################

####################################################
                # range
####################################################

# On l'utilise la plupart du temps pour faire nos boucles for

# values = range(6, 8, 2)          # la fonction range permet de déclarer à l'avance un interval de valeur
#                                  # (falcutatif, par défaut 0) le premier argument donne la position de départ
#                                  # le second argument donne la position d'arrêt
#                                  # (falcutatif, par défaut 1) le troisième argument (step) détermine l'incrémentation

# print(values)

# https://towardsdatascience.com/exploring-python-range-function-d509ebd36ec

####################################################
                # lowercase / uppercase
####################################################

# hello = "Hello"
# print(hello)
# print(hello.lower())
# print(hello.upper())

####################################################
                # sort
####################################################

# fonction pour trier des listes:

# def custom_sort(e):
#     return len(e)

# test_sort = ["cc", "bbbb", "a", "eee", "ddddd", "1234567"]
# print(test_sort)
# test_sort.sort()                            # triera automatiquement par ordre alphabétique (nombre en premier)
# print(test_sort)                     
# test_sort.sort(reverse = True)              # même chose mais en ordre inversé
# print(test_sort) 
# test_sort.sort(key = custom_sort)           # içi on crée une fonction pour renvoyer la liste trier par le nombre de char présents
# print(test_sort) 

####################################################
                # 
####################################################
####################################################
                # 
####################################################
####################################################
                # 
####################################################

def exit_programm():
    print("")
    print("Please press any key to exit the programm.")
    input("")


exit_programm()