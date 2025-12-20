import pyxel
import random

PAC_MONSIEUR = (0, 0, 16, 16)

FANTOME1 = (0, 16, 16, 16)
FANTOME2 = (16, 16, 16, 16)
FANTOME3 = (32, 16, 16, 16)
FANTOME4 = (48, 16, 16, 16)
Fantome_PEUR = (0, 32, 16, 16)
Fantome_yeux = (16, 32, 16, 16)

PETIT_POINT = (0, 48, 16, 16)
GROS_POINT = (16, 48, 16, 16)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Pac-Claudel")
       
        pyxel.load("final-sprites.pyxres")
        
        
        self.petits_points = []

        for y in range(16, 120, 16):
            for x in range(16, 160, 16):
                self.petits_points.append({"x": x, "y": y})
        
        self.score = 0
        self.x = 0
        self.y = 0

        
        self.speed = 2
        
        self.peur = False
        self.peur_timer = 5
        
        
        self.fantomes = [
        {"x": 0,  "y": 16, "sprite": FANTOME1, "état": "normal"},
        {"x": 16, "y": 16, "sprite": FANTOME2, "état": "normal"},
        {"x": 32, "y": 16, "sprite": FANTOME3, "état": "normal"},
        {"x": 48, "y": 16, "sprite": FANTOME4, "état": "normal"},
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
            
        self.x = max(0, min(160 - 16, self.x))
        self.y = max(0, min(120 - 16, self.y))
        
        for p in self.petits_points[:]:
            if abs(self.x - p["x"]) < 16 and abs(self.y - p["y"]) < 16:
                self.petits_points.remove(p)
                self.score += 1 
            
        if abs(self.x - 16) < 16 and abs(self.y - 48) < 16 and not self.peur:
            self.peur = True
            self.peur_timer = 150

        ghost_speed = 0.5

        for i in self.fantomes:
            dx = self.x - i["x"]
            dy = self.y - i["y"]

            
            if self.peur and i["etat"] == "peur":
                if abs(self.x - i["x"]) < 16 and abs(self.y - i["y"]) < 16:
                    i["etat"] = "yeux"
                    i["x"], i["y"] = 80, 56
                    self.score += 50
                    continue

            if i["état"] == "yeux":
                
                if i["x"] < 80:
                    i["x"] += ghost_speed
                elif i["x"] > 80:
                    i["x"] -= ghost_speed

                if i["y"] < 56:
                    i["y"] += ghost_speed
                elif i["y"] > 56:
                    i["y"] -= ghost_speed

                if abs(i["x"] - 80) < 2 and abs(i["y"] - 56) < 2:
                    i["etat"] = "normal"

            elif self.peur:
                i["etat"] = "peur"
            
                if dx > 0:
                    i["x"] -= ghost_speed
                elif dx < 0:
                    i["x"] += ghost_speed

                if dy > 0:
                    i["y"] -= ghost_speed
                elif dy < 0:
                    i["y"] += ghost_speed

            else:
                i["etat"] = "normal"
                
                if dx > 0:
                    i["x"] += ghost_speed
                elif dx < 0:
                    i["x"] -= ghost_speed

                if dy > 0:
                    i["y"] += ghost_speed
                elif dy < 0:
                    i["y"] -= ghost_speed

            
            i["x"] = max(0, min(160 - 16, i["x"]))
            i["y"] = max(0, min(120 - 16, i["y"]))
                    
            if self.peur and i["état"] != "yeux":
                   if abs(self.x - i["x"]) < 16 and abs(self.y - i["y"]) < 16:
                        i["état"] = "yeux"
                        i["x"], i["y"] = 80, 56  # ghost home (center)
                        self.score += 50
                        
            if self.peur:
                self.peur_timer -= 1
                if self.peur_timer <= 0:
                    self.peur = False
        
    def draw(self):
        
        pyxel.cls(0)

        pyxel.blt(self.x, self.y, 0, *PAC_MONSIEUR, 0)
        
        pyxel.text(5, 5, f"SCORE: {self.score}", 7)
     
        for i in self.fantomes:
            if i["etat"] == "yeux":
                pyxel.blt(i["x"], i["y"], 0, *Fantome_yeux, 0)
            elif i["etat"] == "peur":
                pyxel.blt(i["x"], i["y"], 0, *Fantome_PEUR, 0)
            else:
                pyxel.blt(i["x"], i["y"], 0, *i["sprite"], 0)

        
        for p in self.petits_points:
            pyxel.blt(p["x"], p["y"], 0, *PETIT_POINT, 0)
            
        pyxel.blt(16, 48, 0, *GROS_POINT, 0)

App()
