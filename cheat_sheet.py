# Afficher dans la console
# print()

####################################################
                        # print
####################################################

print("Bienvenue dans ce fichier cheat sheet dédié à Python!")
print("ver. 1")
print()

# je peux print des str et des int, 
# mais dans le cas d'un int, il devra être seul ou cast préalablement en str
# on ne peut concaténer un int avec un str autrement

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

####################################################
                # try / except
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

####################################################
                # boucle while
####################################################

# boucle while qui va içi s'effectuer 5 fois

# n = 0

# while n < 5:
#     print("ligne " + str(n))
#     n += 1

# On peut utiliser "not" dans les conditions d'une boucle while

# password = ""

# while not password == "1234":
#     password = input("What is the password? ")

# print("password is correct, you have access to the account.")

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

####################################################
            # 
####################################################

