import pygame

Black = (0, 0, 0, 255)
Bleu = (0, 0, 255, 255)
yellow = (255, 255, 0)

height: int = 25
lenght: int = 25
pixel_size: int = 25
radOfPoint: int = 3
def create_pixel_map(game_map):
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
                pygame.draw.rect(canvas, Bleu,
                                 pygame.Rect(x, y, height, lenght))
                x += lenght
            else:
                pygame.draw.rect(canvas, Black,
                                 pygame.Rect(x, y, height, lenght))
                x += lenght
            if j == len(game_map) - 1:
                y += lenght
                x = 0
def create_point(canvas, game_map,point_list):
    """
    create point n the canva and take ther coordonates
    :param canvas:
    :param game_map:
    :param point_list:
    :return:
    """
    x: int = 0
    y: int = 0
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 0:
                pygame.draw.rect(canvas, yellow,
                                 pygame.Rect(x+10, y+10, radOfPoint, radOfPoint))
                point = (x + 10, y + 10)

                # Vérifier si ce point n'existe pas déjà dans la liste
                if point not in point_list:
                    point_list.append(point)
                x += lenght
            else:
                x += lenght
            if j == len(game_map) - 1:
                y += lenght
                x = 0

def update_point(canvas, list_of_point):
    """
    do the update on the screen each time
    :param canvas:
    :param list_of_point:
    :return:
    """
    for i, point in enumerate(list_of_point):  # Utilisation de `enumerate` pour obtenir l'index et le point
        if point != (0, 0):  # Vérifier si le point n'est pas (0, 0)
            pygame.draw.rect(canvas, yellow,
                             pygame.Rect(point[0], point[1], radOfPoint, radOfPoint))  # Dessiner le point en jaune
        else:
            pygame.draw.rect(canvas, Black,
                             pygame.Rect(point[0], point[1], radOfPoint, radOfPoint))  # Dessiner le point en gris

