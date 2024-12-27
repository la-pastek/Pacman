

def get_sprite_corners(x, y, sprite_width, sprite_height):
    # Coordonnées des coins
    top_left = (x, y)  # Coin haut-gauche
    top_right = (x + sprite_width, y)  # Coin haut-droit
    bottom_left = (x, y + sprite_height)  # Coin bas-gauche
    bottom_right = (x + sprite_width, y + sprite_height)  # Coin bas-droit

    return top_left, top_right, bottom_left, bottom_right


def check_collision(pixel_map, x, y, sprite_width=18, sprite_height=18):
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