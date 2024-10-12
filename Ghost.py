import heapq
import random

# Fonction utilitaire pour Dijkstra
def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    distance = [[float('inf')] * cols for _ in range(rows)]
    prev = [[None] * cols for _ in range(rows)]
    distance[start[1]][start[0]] = 0  # Commencer avec une distance de 0 au point de départ

    pq = [(0, start)]  # (distance, (x, y)) dans une heap pour la file de priorité

    while pq:
        current_distance, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            break  # Chemin trouvé

        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for nx, ny in neighbors:
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == 0:  # S'assurer que la cellule est accessible
                alt = current_distance + 1
                if alt < distance[ny][nx]:
                    distance[ny][nx] = alt
                    prev[ny][nx] = (x, y)
                    heapq.heappush(pq, (alt, (nx, ny)))

    # Reconstruction du chemin
    path = []
    current = goal
    while current and current != start:
        path.append(current)
        current = prev[current[1]][current[0]]

    return path[::-1]  # Retourner le chemin inversé

class Ghost:
    def __init__(self, x, y, speed, pixel_map):
        self.x = x
        self.y = y
        self.speed = speed
        self.pixel_map = pixel_map
        self.path = []
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def get_sprite_corners(self, sprite_width, sprite_height):
        # Coordonnées des coins
        top_left = (self.x, self.y)
        top_right = (self.x + sprite_width, self.y)
        bottom_left = (self.x, self.y + sprite_height)
        bottom_right = (self.x + sprite_width, self.y + sprite_height)

        return top_left, top_right, bottom_left, bottom_right

    def check_collision(self, sprite_width=18, sprite_height=18):
        # Récupérer les coins du sprite
        top_left, top_right, bottom_left, bottom_right = self.get_sprite_corners(sprite_width, sprite_height)

        # Convertir les coordonnées des coins en indices dans la map
        map_x_tl, map_y_tl = top_left[0] // 25, top_left[1] // 25
        map_x_tr, map_y_tr = top_right[0] // 25, top_right[1] // 25
        map_x_bl, map_y_bl = bottom_left[0] // 25, bottom_left[1] // 25
        map_x_br, map_y_br = bottom_right[0] // 25, bottom_right[1] // 25

        # Vérifier la collision pour chaque coin
        if (self.pixel_map[map_y_tl][map_x_tl][0][0] == 1 or
                self.pixel_map[map_y_tr][map_x_tr][0][0] == 1 or
                self.pixel_map[map_y_bl][map_x_bl][0][0] == 1 or
                self.pixel_map[map_y_br][map_x_br][0][0] == 1):
            return True  # Collision détectée
        return False  # Pas de collision

    def move_towards_pacman(self, pacman_x, pacman_y):
        # Convertir les coordonnées de Pac-Man en indices sur la carte
        if pacman_x is not None and pacman_y is not None:
            start = (self.x // 25, self.y // 25)
            goal = (pacman_y // 25, pacman_x // 25)

            # Si le chemin est vide ou non défini, recalculer le chemin avec Dijkstra
            if not self.path:
                self.path = dijkstra(self.pixel_map, start, goal)

            # Vérifier si le fantôme est arrivé à la destination
            if self.path:
                next_position = self.path.pop(0)  # Prendre la prochaine position
                target_x, target_y = next_position[0] * 25, next_position[1] * 25

                # Déplacer vers la prochaine position
                if self.x < target_x:
                    self.x += self.speed
                    self.direction = 'RIGHT'
                elif self.x > target_x:
                    self.x -= self.speed
                    self.direction = 'LEFT'

                if self.y < target_y:
                    self.y += self.speed
                    self.direction = 'DOWN'
                elif self.y > target_y:
                    self.y -= self.speed
                    self.direction = 'UP'

                # Si une collision est détectée, recalculer le chemin
                if self.check_collision():
                    start = (self.x // 25, self.y // 25)
                    self.path = dijkstra(self.pixel_map, start, goal)
        else:
            print("Les coordonnées de Pac-Man ne sont pas valides")

    def draw(self, canvas, ghost_image):
        # Dessiner le fantôme sur le canvas
        canvas.blit(ghost_image, (self.x, self.y))
