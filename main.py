import pygame
from Map.creat_map import create_map
from Map.creat_map import create_pixel_map
from Map.Map_terraformage import The_map
from Map.creat_map import create_point
from Pac import Pac

# Initialisation de Pygame et configuration de l'affichage
pygame.init()
pygame.display.set_caption("Pacman")
canvas = pygame.display.set_mode((500, 500))


The_map_instance = The_map()
game_map = The_map_instance.get_map()  # Collision map

pac = Pac(1, 1, 2, 2)
image = pygame.image.load(r'img.png')
speed_x = 2  # Vitesse de déplacement en pixels
speed_y = 2

# Initialiser l'horloge pour contrôler le framerate
clock = pygame.time.Clock()

def get_sprite_corners(x, y, sprite_width=15, sprite_height=15):
    # Coordonnées des coins
    top_left = (x, y)  # Coin haut-gauche
    top_right = (x + sprite_width, y)  # Coin haut-droit
    bottom_left = (x, y + sprite_height)  # Coin bas-gauche
    bottom_right = (x + sprite_width, y + sprite_height)  # Coin bas-droit

    return top_left, top_right, bottom_left, bottom_right


def check_collision(x, y, sprite_width=18, sprite_height=18):
    # Récupérer les coins du sprite
    top_left, top_right, bottom_left, bottom_right = get_sprite_corners(x, y, sprite_width, sprite_height)

    # Convertir les coordonnées des coins en indices dans la map
    map_x_tl, map_y_tl = top_left[0] // 25, top_left[1] // 25
    map_x_tr, map_y_tr = top_right[0] // 25, top_right[1] // 25
    map_x_bl, map_y_bl = bottom_left[0] // 25, bottom_left[1] // 25
    map_x_br, map_y_br = bottom_right[0] // 25, bottom_right[1] // 25

    # Vérifier la collision pour chaque coin
    if (pixel_map[map_y_tl][map_x_tl][0][0] == 1 or
            pixel_map[map_y_tr][map_x_tr][0][0] == 1 or
            pixel_map[map_y_bl][map_x_bl][0][0] == 1 or
            pixel_map[map_y_br][map_x_br][0][0] == 1):
        return True  # Collision détectée
    return False  # Pas de collision


pixel_map = create_pixel_map(game_map)

def run():
    x = 28
    y = 28
    x_point=0
    y_point=0
    mainloop = True


    while mainloop:
        # Limiter à 60 FPS pour contrôler la vitesse de jeu
        clock.tick(60)  # 60 images par seconde

        create_map(canvas, game_map)  # Crée la carte
        create_point(canvas,game_map,x_point,y_point)
        canvas.blit(image, (y, x))  # Dessine le joueur

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

        # Vérifier les touches pressées pour déplacement continu
        keys = pygame.key.get_pressed()

        # Vérifier les collisions avant d'autoriser les déplacements
        if keys[pygame.K_UP]:
            if not check_collision(x - speed_x, y):  # Vérifie collision vers le haut
                x -= speed_x  # Déplacer seulement si pas de collision
        if keys[pygame.K_DOWN]:
            if not check_collision(x + speed_x, y):  # Vérifie collision vers le bas
                x += speed_x  # Déplacer seulement si pas de collision
        if keys[pygame.K_LEFT]:
            if not check_collision(x, y - speed_y):  # Vérifie collision à gauche
                y -= speed_y  # Déplacer seulement si pas de collision
        if keys[pygame.K_RIGHT]:
            if not check_collision(x, y + speed_y):  # Vérifie collision à droite
                y += speed_y  # Déplacer seulement si pas de collision

        # Mise à jour de l'affichage
        pygame.display.update()

run()
pygame.quit()
