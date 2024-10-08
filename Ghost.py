import random
def get_sprite_corners(self, sprite_width, sprite_height):
    # Coordonnées des coins
    top_left = (self.x, self.y)  # Coin haut-gauche
    top_right = (self.x + sprite_width, self.y)  # Coin haut-droit
    bottom_left = (self.x, self.y + sprite_height)  # Coin bas-gauche
    bottom_right = (self.x + sprite_width, self.y + sprite_height)  # Coin bas-droit

    return top_left, top_right, bottom_left, bottom_right

def check_collision(self, pixel_map, sprite_width=18, sprite_height=18):
    # Récupérer les coins du sprite
    # Coordonnées des coins
    top_left = (self.x, self.y)  # Coin haut-gauche
    top_right = (self.x + sprite_width, self.y)  # Coin haut-droit
    bottom_left = (self.x, self.y + sprite_height)  # Coin bas-gauche
    bottom_right = (self.x + sprite_width, self.y + sprite_height)  # Coin bas-droit

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
class Ghost:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])


    def move_towards_pacman(self, pacman_x, pacman_y,pixel_map):
        """
        this function check also the collision with the wall
        :param pacman_x:
        :param pacman_y:
        :return:
        """
        diff_x = pacman_y - self.x
        diff_y = pacman_x - self.y


        # Calculer la différence entre le fantôme et Pac-Man
        # Priorité : déplacez-vous dans la direction où la distance est la plus grande
        if abs(diff_x) > abs(diff_y) :
            if diff_x > 0 and not check_collision(self,pixel_map):
                self.x += self.speed  # Déplacer vers la droite
                self.direction = "RIGHT"
            elif diff_x< 0 and check_collision(self,pixel_map):
                self.x -= self.speed  # Déplacer vers la gauche
                self.direction = "Left"
        else:
            if diff_y > 0 and not check_collision(self,pixel_map):
                self.y += self.speed  # Déplacer vers le bas
                self.direction = "DOWN"
            elif diff_y<0 and not check_collision(self,pixel_map):
                self.y -= self.speed  # Déplacer vers le haut
                self.direction = "UP"

    def draw(self, canvas, ghost_image):
        # Dessiner le fantôme sur le canvas
        canvas.blit(ghost_image, (self.x, self.y))