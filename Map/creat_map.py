import pygame


BackGround_gray0 = (190, 190, 190, 255)
rect_color = (255, 0, 0)

height: int = 25
lenght: int = 25



def posMap(game_map,xpos,ypos):
    x, y = 0,0
    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                x+=25
                y+=25
                x_pos.append(x)
                y_pos.append(y)
    print(x_pos,y_pos,"ok")



def create_map(canvas, game_map):
    x: int = 0
    y: int = 0

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            if game_map[i][j] == 1:
                pygame.draw.rect(canvas, rect_color,
                                 pygame.Rect(x, y, height, lenght))
                x += lenght
            else:
                pygame.draw.rect(canvas, BackGround_gray0,
                                 pygame.Rect(x, y, height, lenght))
                x += lenght
            if j == len(game_map) - 1:
                y += lenght
                x = 0