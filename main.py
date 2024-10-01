from turtledemo import clock
import pygame
from creat_map import create_map
from Pac import Pac

pygame.init()
pygame.display.set_caption("Show Image")
canvas = pygame.display.set_mode((500, 500))
create_map(canvas)

yellow = ((255, 255, 0))

pac = Pac(1, 1, 2, 2)
image = pygame.image.load(r'img.png')
speed_x = 1
speed_y = 1


def run():
    x = 100
    y = 100
    mainloop = True

    while mainloop:
        create_map(canvas)
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
            x -= speed_x
        if keys[pygame.K_DOWN]:
            x += speed_x
        if keys[pygame.K_LEFT]:
            y -= speed_y
        if keys[pygame.K_RIGHT]:
            y += speed_y

        # Mise à jour de l'affichage
        pygame.display.update()


run()
pygame.quit()
