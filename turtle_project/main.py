####################################################
                    # import
####################################################

import turtle               # j'importe mon module

####################################################
                    # ?
####################################################

t = turtle.Turtle()         # j'initialise une variable t, nécessaire au module

####################################################
                    # Instructions
####################################################

# ...                       les instructions pour déplacer la tortue

# t.forward(100)             # faire avancer la tortue (en pixel)
# t.backward(100)            # faire reculer la tortue (en pixel)

# t.right(90)                  # faire pivoter la tortue sur la droite (en degrés)
# t.left(90)                   # faire pivoter la tortue sur la gauche (en degrés)

####################################################
                    # functions 
####################################################

# Dessine des marches d'escalier
def draw_stair(size, nb_of_stair):
    for i in range(0, (nb_of_stair - 1)):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)


# Dessine un carré
def draw_square(size):
    for i in range(0, 4):
        t.forward(size)
        t.left(90)


# Dessine de multiples carrés
def draw_squares(beginning_size, nb_of_square):
    for i in range(0, nb_of_square):
        draw_square(beginning_size)
        beginning_size += 10






####################################################
                    # Exécution
####################################################

# draw_stair(30, 5)
# draw_square(50)
draw_squares(10, 3)

turtle.done()               # empêche la fenêtre graphique de se fermer