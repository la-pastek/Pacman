from unittest import TestCase
import unittest

# Fonction à tester
def compare_positions(x, y, x_pos, y_pos):
    # Boucler sur les éléments de x_pos et y_pos
    for i in range(len(x_pos)):
        # Boucle pour vérifier toutes les valeurs de x_pos[i] - 25 à x_pos[i]
        for j in range(26):
            adjusted_x = x_pos[i] - j
            adjusted_y = y_pos[i] - j
            print(adjusted_x, "ad x")
            print(adjusted_y,"ad y")
            if x == adjusted_x and y == adjusted_y:
                print("MATCH")
                return True

    # Si aucune correspondance n'est trouvée, retourner False
    return False

class TestComparePositions(TestCase):


    def test_position_match(self):
        x_pos = [0, 25, 50]
        y_pos = [0, 25, 50]
        # Test avec correspondance
        self.assertTrue(compare_positions(25, 25, x_pos, y_pos))

    def test_position_no_match(self):
        x_pos = [0, 25, 50]
        y_pos = [0, 25, 50]
        # Test sans correspondance
        self.assertFalse(compare_positions(10, 25, x_pos, y_pos))

    def test_border_case(self):
        x_pos = [0, 25, 50]
        y_pos = [0, 25, 50]
        # Test avec correspondance à la limite (x_pos - 25)
        self.assertTrue(compare_positions(0, 0, x_pos, y_pos))

    def test_no_positions(self):
        # Test avec des listes vides
        self.assertFalse(compare_positions(10, 10, [], []))

