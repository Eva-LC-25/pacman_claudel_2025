# Code Python
import math
import random
import pyxel
pos_player = [76, 56]

fond = 8
def update():
    #logique du jeu
    global pos_player,fond    #Touche flèche droite
    if pyxel.btn(pyxel.KEY_RIGHT):
        pos_player[0] += 1
    #Touche flèche gauche
    if pyxel.btn(pyxel.KEY_LEFT):
        pos_player[0] -= 1
    #Touche flèche haut
    if pyxel.btn(pyxel.KEY_UP):
        pos_player[1] -= 1
    #Touche flèche bas
    if pyxel.btn(pyxel.KEY_DOWN):
        pos_player[1] += 1
        

def draw():
    pyxel.cls(fond) #fond
    pyxel.rect(pos_player[0], pos_player[1], 4, 4, 11)
    pyxel.rect(0, 110, 160, 10, 2) # name
    pyxel.rect(0, 0, 160, 10, 2)
    pyxel.rect(0, 0, 10, 50, 2)
    pyxel.rect(0, 60, 10, 60, 2)
    pyxel.rect(150, 0, 10, 50, 2)
    pyxel.rect(150, 60, 10, 60, 2)
    pyxel.rect(0, 50, 10 ,10 , 7)
#     pyxel.rect(x_carre2, y_carre2, 4, 4, 3)
pyxel.init(160, 120, title="mon premier jeu")
pyxel.run(update, draw)
