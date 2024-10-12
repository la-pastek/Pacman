import heapq
import random

# Fonction utilitaire pour Dijkstra
import heapq

def dijkstra(pixel_map, start, goal):
    rows, cols = len(pixel_map), len(pixel_map[0])
    # Créer une matrice pour garder une trace des distances minimales
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0  # Distance de départ est 0

    # Créer un tableau pour garder une trace des nœuds précédents pour reconstruire le chemin
    previous_nodes = [[None] * cols for _ in range(rows)]

    # Priority queue pour gérer les nœuds à explorer
    priority_queue = [(0, start)]  # (distance, (row, col))

    # Directions possibles (haut, bas, gauche, droite)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # DOWN, UP, RIGHT, LEFT

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        current_row, current_col = current_node

        # Si on atteint la destination, reconstruire le chemin
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node[0]][current_node[1]]
            return path[::-1]  # Retourner le chemin inversé

        # Si une distance plus courte a déjà été trouvée, ignorer
        if current_distance > distances[current_row][current_col]:
            continue

        # Explorer les voisins
        for direction in directions:
            neighbor_row = current_row + direction[0]
            neighbor_col = current_col + direction[1]

            # Vérifier que le voisin est dans les limites et pas un mur
            if (0 <= neighbor_row < rows and
                    0 <= neighbor_col < cols and
                    pixel_map[neighbor_row][neighbor_col][0][0] == 0):  # Vérifie si ce n'est pas un mur
                new_distance = current_distance + 1  # Coût d'un mouvement

                # Si une distance plus courte est trouvée, mettre à jour
                if new_distance < distances[neighbor_row][neighbor_col]:
                    distances[neighbor_row][neighbor_col] = new_distance
                    previous_nodes[neighbor_row][neighbor_col] = (current_row, current_col)
                    heapq.heappush(priority_queue, (new_distance, (neighbor_row, neighbor_col)))

    return []  # Retourner un chemin vide si aucun chemin n'est trouvé

class Ghost:
    def __init__(self, x, y, speed, pixel_map):
        self.x = x
        self.y = y
        self.speed = speed
        self.pixel_map = pixel_map
        self.path = []
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def move_towards_pacman(self, pacman_x, pacman_y):
        # Convertir les coordonnées de Pac-Man en indices sur la carte
        if pacman_x is not None and pacman_y is not None:
            start = (self.x // 25, self.y // 25)
            goal = (pacman_y // 25, pacman_x // 25)  # Inversé car y correspond à x

            # Si le chemin est vide ou non défini, recalculer le chemin avec Dijkstra
            if not self.path:
                self.path = dijkstra(self.pixel_map, start, goal)

            # Vérifier si le fantôme est arrivé à la destination
            if self.path:
                next_position = self.path[0]  # Prendre la prochaine position
                target_x, target_y = next_position[0] * 25, next_position[1] * 25

                # Vérifier les collisions avant de bouger

                # Si pas de collision, déplacer le fantôme
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

                # Si le fantôme atteint la prochaine position, la retirer de la liste
                if self.x == target_x and self.y == target_y:
                    self.path.pop(0)

    def draw(self, canvas, ghost_image):
        # Dessiner le fantôme sur le canvas
        canvas.blit(ghost_image, (self.x, self.y))
