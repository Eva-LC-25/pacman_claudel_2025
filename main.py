# Pyxel Studio
import pygame
import math
import pyxel
import random

pos_player = [76, 56]
x= 56
y= 70
LCARRE = 4

def update():
    #logique du jeu
    global pos_player,fond,x,y
    dx = 0
    dy = 0
    #deplacement avec les fleches
    if pyxel.btn(pyxel.KEY_RIGHT):
        dx = 1
    if pyxel.btn(pyxel.KEY_LEFT):
        dx = -1
    if pyxel.btn(pyxel.KEY_UP):
        dy = -1
    if pyxel.btn(pyxel.KEY_DOWN):
        dy = 1
    x+=dx
    y+=dy
    print (x,y)
    
    #collision
    if  pyxel.pget(x, y) == 8 or pyxel.pget(x + LCARRE - 1, y) == 8 or pyxel.pget(x, y + LCARRE - 1) == 8 or pyxel.pget(x + LCARRE - 1, y + LCARRE - 1) == 8:
        x -= dx
        y -= dy
    
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    
    #teleporting function
    if x <= -3 and y in range (56,69):
        x = 127
    if x >= 128 and y in range (56,69):
        x = -2


def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
    pyxel.rect(x, y, LCARRE, LCARRE, 9)
#     pyxel.rect(x_carre2, y_carre2, 4, 4, 3)
    
pyxel.init(128, 128, title="mon premier jeu")
pyxel.load("res.pyxres")
pyxel.run(update, draw)
    
pyxel.init(128, 128, title="mon premier jeu")
pyxel.load("res.pyxres")
pyxel.run(update, draw)
