import pygame

from Ghost import Ghost
from Map.creat_map import create_map
from Map.creat_map import create_pixel_map
from Map.creat_map import update_point
from Map.creat_map import create_point


from Map.Map_terraformage import The_map

from Pac import Pac

# Initialisation de Pygame et configuration de l'affichage
pygame.init()
pygame.display.set_caption("Pacman")
canvas = pygame.display.set_mode((500, 500))

The_map_instance = The_map()
game_map = The_map_instance.get_map()  # Collision map

pac = Pac(1, 1, 2, 2)
image_sprite = [pygame.image.load("File_img/img4.png"),
                pygame.image.load("File_img/img3.png"),
                pygame.image.load("File_img/img2.png")
                ]
speed_x = 2  # Vitesse de déplacement en pixels
speed_y = 2

# Initialiser l'horloge pour contrôler le framerate
clock = pygame.time.Clock()


def get_sprite_corners(x, y, sprite_width, sprite_height):
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



def check_collisionPoint(x, y, list, sprite_width=18, sprite_height=18, margin=5):
    # Récupérer les coins du sprite
    top_left, top_right, bottom_left, bottom_right = get_sprite_corners(x, y, sprite_width, sprite_height)

    # Convertir les coordonnées des coins en indices dans la map avec ajustements
    map_x_tl, map_y_tl = top_left[0] + 7, top_left[1] + 7
    map_x_tr, map_y_tr = top_right[0] - 11, top_right[1] + 7
    map_x_bl, map_y_bl = bottom_left[0] + 7, bottom_left[1] - 11
    map_x_br, map_y_br = bottom_right[0] - 11, bottom_right[1] - 11

    # Créer une liste des coordonnées des coins du sprite
    corners = [(map_x_tl, map_y_tl), (map_x_tr, map_y_tr),
               (map_x_bl, map_y_bl), (map_x_br, map_y_br)]

    # Parcourir les coins du sprite
    for corner in corners:
        for i, point in enumerate(list):  # Utilisation de enumerate pour obtenir l'index du point
            # Vérifier si le point est à une distance de margin pixels autour du coin
            if abs(corner[0] - point[0]) <= margin and abs(corner[1] - point[1]) <= margin:
                print("Collision détectée avec le point:", point)
                # Remplacer le point dans la liste par (0, 0)
                list[i] = (0, 0)
                return True  # Une collision a été détectée et traitée

    return False  # Pas de collision détectée


pixel_map = create_pixel_map(game_map)

ghosts = [
    Ghost(200, 250, 1,pixel_map),  # Ajouter des fantômes avec des coordonnées et une vitesse initiales
    Ghost(250, 275, 1,pixel_map)
]
ghost_image = pygame.image.load("File_img/ghost.png")
def run():
    global image
    x = 28
    y = 28
    moving = False
    value = 0
    point_listXY = []
    create_point(canvas, game_map, point_listXY)
    # Variables pour gérer l'animation
    animation_frame_time = 0
    animation_speed = 5  # Plus ce nombre est élevé, plus l'animation est lente
    mainloop = True
    direction = "DOWN"  # Direction initiale
    # Pivoter l'image selon la direction

    while mainloop:
        # Limiter à 60 FPS pour contrôler la vitesse de jeu
        clock.tick(60)  # 60 images par seconde

        create_map(canvas, game_map)  # Crée la carte
        check_collisionPoint(x, y, point_listXY)
        update_point(canvas, point_listXY)

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
                moving = True
                x -= speed_x  # Déplacer seulement si pas de collision
                direction = "UP"  # Changer la direction
        if keys[pygame.K_DOWN]:
            if not check_collision(x + speed_x, y):  # Vérifie collision vers le bas
                moving = True
                x += speed_x  # Déplacer seulement si pas de collision
                direction = "DOWN"  # Changer la direction
        if keys[pygame.K_LEFT]:
            if not check_collision(x, y - speed_y):  # Vérifie collision à gauche
                moving = True
                y -= speed_y  # Déplacer seulement si pas de collision
                direction = "LEFT"  # Changer la direction
        if keys[pygame.K_RIGHT]:
            if not check_collision(x, y + speed_y):  # Vérifie collision à droite
                moving = True
                y += speed_y  # Déplacer seulement si pas de collision
                direction = "RIGHT"  # Changer la direction
        # Mettre à jour l'animation
        if moving:
            animation_frame_time += 1
            if animation_frame_time >= animation_speed:  # Change l'image selon le speed
                value += 1
                animation_frame_time = 0
                if value >= len(image_sprite):
                    value = 0  # Réinitialiser l'animation
        if direction == "UP":
            image = pygame.transform.rotate(image_sprite[value], 90)
        elif direction == "DOWN":
            image = pygame.transform.rotate(image_sprite[value], 270)
        elif direction == "LEFT":
            image = pygame.transform.rotate(image_sprite[value], 180)
        elif direction == "RIGHT":
            image = image_sprite[value]  # Pas de rotation

        canvas.blit(image, (y, x))  # Dessine le joueur

        ghosts[0].move_towards_pacman(x, y)
        ghosts[0].draw(canvas, ghost_image)

        ghosts[1].move_towards_pacman(x, y)
        ghosts[1].draw(canvas, ghost_image)
        #ghost.move_towards_pacman(x, y,pixel_map)  # Déplacer le fantôme vers Pac-Man
        #ghost.draw(canvas, ghost_image)  # Dessiner le fantôme
        # Mise à jour de l'affichage
        pygame.display.update()


run()
pygame.quit()
