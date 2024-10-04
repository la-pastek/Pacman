import pygame

BackGround_gray0 = (190, 190, 190, 255)
rect_color = (255, 0, 0)
yellow = ((255, 255, 0))

height: int = 25
lenght: int = 25

def create_pixel_map(game_map, pixel_size=25):
    rows = len(game_map)
    cols = len(game_map[0]) if rows > 0 else 0
    pixel_map = []

    for i in range(rows):
        pixel_row = []
        for j in range(cols):
            value = 1 if game_map[i][j] == 1 else 0
            pixel_block = [[value] * pixel_size for _ in range(pixel_size)]
            pixel_row.append(pixel_block)
        pixel_map.append(pixel_row)

    return pixel_map

def create_map(canvas, game_map):
    x: int = 0
    y: int = 0

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                pygame.draw.rect(canvas, rect_color,
                                 pygame.Rect(y, x, height, lenght))
                x += lenght
            else:
                pygame.draw.rect(canvas, BackGround_gray0,
                                 pygame.Rect(y, x, height, lenght))

                x += lenght
            if j == len(game_map) - 1:
                y += lenght
                x = 0
def  create_point(canvas, game_map,x_point,y_point):
    x: int = 0
    y: int = 0
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            x_point = x
            y_point = y
            if game_map[i][j] == 0:
                pygame.draw.rect(canvas, yellow,
                                 pygame.Rect(y+10, x+10, 3, 3))
                x += lenght
            else:
                x += lenght
            if j == len(game_map) - 1:
                y += lenght
                x = 0
