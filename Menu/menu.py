import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)



def start_menu(canvas, mainloop):

    while mainloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    mainloop = False
        canvas.fill(WHITE)
        pygame.draw.rect(canvas, RED, [200, 200, 100, 100])

        pygame.display.update()