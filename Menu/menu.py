import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
Black = (0, 0, 0, 255)


def start_menu(canvas, mainloop):
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render('tape space to start', True, green, blue)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (400, 400)
    while mainloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    mainloop = False
        canvas.fill(Black)
        canvas.blit(text, textRect)

        pygame.display.update()