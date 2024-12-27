import pygame

from character.Ghost import Ghost
from Map.creat_map import create_map
from Map.creat_map import create_pixel_map
from Map.creat_map import update_point
from Map.creat_map import create_point
from Utils import Collision
from Menu import menu
from Map.Map_terraformage import The_map


# Initialisation de Pygame et configuration de l'affichage
pygame.init()
pygame.display.set_caption("Pacman")
canvas = pygame.display.set_mode((800, 800))

The_map_instance = The_map()
game_map = The_map_instance.get_map()  # Collision map



image_sprite = [pygame.image.load("File_img/img4.png"),
                pygame.image.load("File_img/img3.png"),
                pygame.image.load("File_img/img2.png")
                ]
speed_x = 2  # Vitesse de déplacement en pixels
speed_y = 2

# Initialiser l'horloge pour contrôler le framerate
clock = pygame.time.Clock()

pixel_map = create_pixel_map(game_map)

ghosts = [
    Ghost(200, 250, 1, pixel_map),  # Ajouter des fantômes avec des coordonnées et une vitesse initiales
    Ghost(250, 275, 1, pixel_map),
    Ghost(275, 300, 1, pixel_map),
    Ghost(300, 325, 1, pixel_map)
]
ghost_image = pygame.image.load("File_img/ghost.png")
def run():
    global image
    x = 28
    y = 28

    point_listXY = []
    create_point(canvas, game_map, point_listXY)

    # Creation des variables
    mainloop = True # a declarer false a la fin d'une partie
    menu.start_menu(canvas, mainloop)
    moving = False
    value = 0
    animation_frame_time = 0
    animation_speed = 5  # Plus ce nombre est élevé, plus l'animation est lente
    direction = "DOWN"  # Direction initiale

    while mainloop:
        # Limiter à 60 FPS pour contrôler la vitesse de jeu
        clock.tick(60)  # 60 images par seconde

        create_map(canvas, game_map)  # Crée la carte
        Collision.check_collisionPoint(x, y, point_listXY) # quand le pacman pâsse dessus enregistre la position X et Y
        update_point(canvas, point_listXY) # la map est actualiser en retirant les points point_litXY

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
        if keys[pygame.K_LEFT]:
            if not Collision.check_collision(pixel_map,x - speed_x, y):  # Vérifie collision vers le haut
                moving = True
                x -= speed_x  # Déplacer seulement si pas de collision
                direction = "LEFT"  # Changer la direction
        if keys[pygame.K_RIGHT]:
            if not Collision.check_collision(pixel_map, x + speed_x, y):  # Vérifie collision vers le bas
                moving = True
                x += speed_x  # Déplacer seulement si pas de collision
                direction = "RIGHT"  # Changer la direction
        if keys[pygame.K_UP]:
            if not Collision.check_collision(pixel_map,x, y - speed_y):  # Vérifie collision à gauche
                moving = True
                y -= speed_y  # Déplacer seulement si pas de collision
                direction = "UP"  # Changer la direction
        if keys[pygame.K_DOWN]:
            if not Collision.check_collision(pixel_map,x, y + speed_y):  # Vérifie collision à droite
                moving = True
                y += speed_y  # Déplacer seulement si pas de collision
                direction = "DOWN"  # Changer la direction
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

        canvas.blit(image, (x, y))  # Dessine le joueur

        #dessine les fantomes
        ghosts[0].move_towards_pacman(x, y)
        ghosts[0].draw(canvas, ghost_image)
        ghosts[1].move_towards_pacman(x, y)
        ghosts[1].draw(canvas, ghost_image)
        ghosts[2].move_towards_pacman(x, y)
        ghosts[2].draw(canvas, ghost_image)
        ghosts[3].move_towards_pacman(x, y)
        ghosts[3].draw(canvas, ghost_image)


        #ghost.move_towards_pacman(x, y,pixel_map)  # Déplacer le fantôme vers Pac-Man
        #ghost.draw(canvas, ghost_image)  # Dessiner le fantôme
        # Mise à jour de l'affichage
        pygame.display.update()


run()
pygame.quit()
