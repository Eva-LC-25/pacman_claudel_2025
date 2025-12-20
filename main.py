import pyxel
import random

PAC_MONSIEUR = (0, 0, 16, 16)

FANTOME1 = (0, 16, 16, 16)
FANTOME2 = (16, 16, 16, 16)
FANTOME3 = (32, 16, 16, 16)
FANTOME4 = (48, 16, 16, 16)

PETIT_POINT = (0, 48, 16, 16)
GROS_POINT = (16, 48, 16, 16)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Pac-Claudel")

       
        pyxel.load("final-sprites.pyxres")
        
        self.x = 0
        self.y = 0

        
        self.speed = 2
        
        self.fantomes = [
            {"x": 0,  "y": 16, "dx": 1,  "dy": 0, "timer": 0, "sprite": FANTOME1},
            {"x": 16, "y": 16, "dx": 0,  "dy": 1, "timer": 0, "sprite": FANTOME2},
            {"x": 32, "y": 16, "dx": -1, "dy": 0, "timer": 0, "sprite": FANTOME3},
            {"x": 48, "y": 16, "dx": 0,  "dy": -1, "timer": 0, "sprite": FANTOME4},
        ]

        pyxel.run(self.update, self.draw)

    def update(self):
        
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed
            
        fantomes_speed = 0.5
        cercle_detection = 40

        for i in self.fantomes:
            dx = self.x - i["x"]
            dy = self.y - i["y"]

    
        if abs(dx) < cercle_detection and abs(dy) < cercle_detection:
           
            if dx > 0:
                i["x"] += fantomes_speed
            elif dx < 0:
                i["x"] -= fantomes_speed

            if dy > 0:
                i["y"] += fantomes_speed
            elif dy < 0:
                i["y"] -= fantomes_speed
        else:
           
            if i["timer"] <= 0:
                i["dx"] = pyxel.rndi(-1, 1)
                i["dy"] = pyxel.rndi(-1, 1)
                i["timer"] = 30

            i["x"] += i["dx"]
            i["y"] += i["dy"]
            i["timer"] -= 1
        
        
        

    def draw(self):
        
        pyxel.cls(0)

        pyxel.blt(self.x, self.y, 0, *PAC_MONSIEUR, 0)
     
        for i in self.fantomes:
            pyxel.blt(i["x"], i["y"], 0, *i["sprite"], 0)

        
        pyxel.blt(0, 48, 0, *PETIT_POINT, 0)
        pyxel.blt(16, 48, 0, *GROS_POINT, 0)
        
        for i in self.fantomes:
            pyxel.blt(i["x"], i["y"], 0, *i["sprite"], 0)

