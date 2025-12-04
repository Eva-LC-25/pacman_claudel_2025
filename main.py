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

import pyxel
import random
import math

LARGEUR = 200
HAUTEUR = 200

# --- Distance entre pacman et fantôme
def distance(p1, p2):
    return math.sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

class Jeu:
    def __init__(self):
        pyxel.init(LARGEUR, HAUTEUR, title="Pac-Man Pyxel")

        # Pac-Man
        self.pacman = {"x": 100, "y": 100, "size": 8}

        # Fantômes
        self.fantome_vitesse = 1
        self.fantomes = []

        for i in range(5):
            fx = random.randint(10, LARGEUR - 10)
            fy = random.randint(10, HAUTEUR - 10)
            self.fantomes.append({
                "x": fx,
                "y": fy,
                "dir": [0, 0],
                "timer": 0
            })

        pyxel.run(self.update, self.draw)

    def update(self):
        # --- Déplacement Pac-Man
        if pyxel.btn(pyxel.KEY_LEFT):
            self.pacman["x"] -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.pacman["x"] += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.pacman["y"] -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.pacman["y"] += 1

        # Limites écran
        self.pacman["x"] = max(0, min(self.pacman["x"], LARGEUR))
        self.pacman["y"] = max(0, min(self.pacman["y"], HAUTEUR))

        # --- IA des fantômes
        for f in self.fantomes:
            d = distance(self.pacman, f)

            if d < 40:  # Détection
                if self.pacman["x"] > f["x"]:
                    f["x"] += self.fantome_vitesse
                if self.pacman["x"] < f["x"]:
                    f["x"] -= self.fantome_vitesse
                if self.pacman["y"] > f["y"]:
                    f["y"] += self.fantome_vitesse
                if self.pacman["y"] < f["y"]:
                    f["y"] -= self.fantome_vitesse

            else:
                # Déplacement aléatoire
                if f["timer"] <= 0:
                    f["dir"] = [
                        random.choice([-1, 0, 1]),
                        random.choice([-1, 0, 1])
                    ]
                    f["timer"] = 20

                f["x"] += f["dir"][0] * self.fantome_vitesse
                f["y"] += f["dir"][1] * self.fantome_vitesse
                f["timer"] -= 1

                # Reste dans la fenêtre
                f["x"] = max(0, min(f["x"], LARGEUR))
                f["y"] = max(0, min(f["y"], HAUTEUR))

    def draw(self):
        pyxel.cls(0)

        # Pac-Man (jaune)
        pyxel.rect(self.pacman["x"], self.pacman["y"], self.pacman["size"], self.pacman["size"], 10)

        # Fantômes (rouges)
        for f in self.fantomes:
            pyxel.rect(f["x"], f["y"], 8, 8, 8)
