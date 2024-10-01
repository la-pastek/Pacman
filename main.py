import pygame
from Map.creat_map import create_map
from Map.Map_terraformage import The_map
from Pac import Pac


pygame.init()
pygame.display.set_caption("Show Image")
canvas = pygame.display.set_mode((500, 500))

The_map_instance = The_map()
game_map = The_map_instance.get_map()
create_map(canvas, game_map)


yellow = ((255, 255, 0))

pac = Pac(1, 1, 2, 2)
image = pygame.image.load(r'img.png')
speed_x = 1
speed_y = 1

def check_collision(x, y):
    """ Vérifie si la nouvelle position (x, y) est libre. """
    # Convertir les coordonnées en indices de la matrice
    map_x = y // 25  # Adaptez ces valeurs selon la taille de votre case
    map_y = x // 25  # Adaptez ces valeurs selon la taille de votre case
    if 0 <= map_x < len(game_map) and 0 <= map_y < len(game_map[0]):
        return game_map[map_x][map_y] == 0  # Retourne True si la case est libre
    return False  # En dehors des limites de la carte
def run():
    x = 25
    y = 25
    mainloop = True

    while mainloop:
        create_map(canvas,game_map)
        canvas.blit(image, (y, x))

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

        # Vérifier les touches pressées pour déplacement continu
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if check_collision(x - speed_x, y):  # Vérifier avant de déplacer
                x -= speed_x
        if keys[pygame.K_DOWN]:
            if check_collision(x + speed_x, y):  # Vérifier avant de déplacer
                x += speed_x
        if keys[pygame.K_LEFT]:
            if check_collision(x, y - speed_y):  # Vérifier avant de déplacer
                y -= speed_y
        if keys[pygame.K_RIGHT]:
            if check_collision(x, y + speed_y):  # Vérifier avant de déplacer
                y += speed_y

        # Mise à jour de l'affichage
        pygame.display.update()


run()
pygame.quit()
