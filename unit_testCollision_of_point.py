import unittest

def get_sprite_corners(x, y, sprite_width, sprite_height):
    # Coordonnées des coins
    top_left = (x, y)  # Coin haut-gauche
    top_right = (x + sprite_width, y)  # Coin haut-droit
    bottom_left = (x, y + sprite_height)  # Coin bas-gauche
    bottom_right = (x + sprite_width, y + sprite_height)  # Coin bas-droit

    return top_left, top_right, bottom_left, bottom_right
def check_collisionPoint(x, y, x_list_point, y_list_point, sprite_width=18, sprite_height=18):
    # Récupérer les coins du sprite
    top_left, top_right, bottom_left, bottom_right = get_sprite_corners(x, y, sprite_width, sprite_height)

    # Convertir les coordonnées des coins en indices dans la map
    map_x_tl, map_y_tl = top_left[0], top_left[1]
    map_x_tr, map_y_tr = top_right[0], top_right[1]
    map_x_bl, map_y_bl = bottom_left[0], bottom_left[1]
    map_x_br, map_y_br = bottom_right[0], bottom_right[1]

    # Créer une liste des coordonnées des coins du sprite
    corners = [(map_x_tl, map_y_tl), (map_x_tr, map_y_tr),
               (map_x_bl, map_y_bl), (map_x_br, map_y_br)]


    # Parcourir les coins du sprite
    for corner in corners:
        print(corners[0], "corner 0")
        print(corners[1], "corner 1")
        print(x_list_point,"x list")
        print(y_list_point, "y list")
        if corner[0] in x_list_point and corner[1] in y_list_point:
            # Trouver l'indice correspondant
            index_x = x_list_point.index(corner[0])
            index_y = y_list_point.index(corner[1])


            # Vérifier si les indices de x et y correspondent
            if index_x == index_y:
                # Supprimer les coordonnées de la liste
                x_list_point.pop(index_x)
                y_list_point.pop(index_y)

                return True  # Une collision a été détectée et traitée

    return False  # Pas de collision détectée


class TestCollisionDetection(unittest.TestCase):

    def test_collision_detected(self):
        # Définir les paramètres d'entrée
        x, y = 100, 100
        x_list_point = [100, 120, 130]
        y_list_point = [100, 120, 130]
        sprite_width = 18
        sprite_height = 18

        # Appel de la fonction check_collisionPoint
        result = check_collisionPoint(x, y, x_list_point, y_list_point, sprite_width, sprite_height)

        # Vérifier que la fonction retourne True (collision détectée)
        self.assertTrue(result)

        # Vérifier que les points correspondants ont bien été supprimés des listes
        self.assertNotIn(100, x_list_point)
        self.assertNotIn(100, y_list_point)

    def test_no_collision(self):
        # Définir les paramètres d'entrée
        x, y = 150, 150
        x_list_point = [100, 120, 130]
        y_list_point = [100, 120, 130]
        sprite_width = 18
        sprite_height = 18

        # Appel de la fonction check_collisionPoint
        result = check_collisionPoint(x, y, x_list_point, y_list_point, sprite_width, sprite_height)

        # Vérifier que la fonction retourne False (pas de collision)
        self.assertFalse(result)

        # Vérifier que les listes n'ont pas été modifiées
        self.assertEqual(x_list_point, [100, 120, 130])
        self.assertEqual(y_list_point, [100, 120, 130])

    def test_empty_list(self):
        # Définir les paramètres d'entrée
        x, y = 100, 100
        x_list_point = []
        y_list_point = []
        sprite_width = 18
        sprite_height = 18

        # Appel de la fonction check_collisionPoint
        result = check_collisionPoint(x, y, x_list_point, y_list_point, sprite_width, sprite_height)

        # Vérifier que la fonction retourne False (pas de collision)
        self.assertFalse(result)

        # Vérifier que les listes sont toujours vides
        self.assertEqual(x_list_point, [])
        self.assertEqual(y_list_point, [])


