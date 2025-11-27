# Pyxel Studio
import pyxel

pos_player = [76, 56]

def update():
    #logique du jeu
    #global pos_player,fond    #Touche flèche droite
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
    
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
    pyxel.rect(pos_player[0], pos_player[1], 4, 4, 9)
#     pyxel.rect(x_carre2, y_carre2, 4, 4, 3)
    
pyxel.init(128, 128, title="mon premier jeu")
pyxel.load("res.pyxres")
pyxel.run(update, draw)
