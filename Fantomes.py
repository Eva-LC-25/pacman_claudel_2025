import pygame
import random
import math

pygame.init()

longueur, hauteur = 600, 600
win = pygame.display.set_mode((longueur, hauteur))
clock = pygame.time.Clock()

pacman = pygame.Rect(300, 300, 20, 20)

# Fonction distance
def distance(r1, r2):
    return math.sqrt((r1.x - r2.x)**2 + (r1.y - r2.y)**2)

# Création des fantômes
fantomes = []
fantome_vitesse = 2

for i in range(5):
    x = random.randint(50, longueur - 50)
    y = random.randint(50, hauteur - 50)
    fantomes.append({
        "rect": pygame.Rect(x, y, 20, 20),
        "dir": [0, 0],
        "timer": 0
    })

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement des fantômes
    for fantome in fantomes:
        rect = fantome["rect"]
        d = distance(pacman, rect)

        if d < 120:
            # Fantôme poursuit Pacman
            if pacman.x > rect.x: rect.x += fantome_vitesse
            if pacman.x < rect.x: rect.x -= fantome_vitesse
            if pacman.y > rect.y: rect.y += fantome_vitesse
            if pacman.y < rect.y: rect.y -= fantome_vitesse

        else:
            # Déplacement aléatoire
            if fantome["timer"] == 0:
                fantome["dir"] = [
                    random.choice([-1, 0, 1]),
                    random.choice([-1, 0, 1])
                ]
                fantome["timer"] = 20

            rect.x += fantome["dir"][0] * fantome_vitesse
            rect.y += fantome["dir"][1] * fantome_vitesse
            fantome["timer"] -= 1

        # Empêcher les fantômes de sortir de l'écran
        rect.x = max(0, min(longueur - 20, rect.x))
        rect.y = max(0, min(hauteur - 20, rect.y))

    # Affichage
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 255, 0), pacman)
    for fantome in fantomes:
        pygame.draw.rect(win, (255, 0, 0), fantome["rect"])

    pygame.display.update()

pygame.quit()