#!/usr/bin/env python3

# --------------------------
# Imports
# --------------------------
# The unit testing framework
import unittest
# The objects under test
from room import Room
from polygon import Polygon
from furniture import Furniture

class SimplePolygonTestCase(unittest.TestCase):
    def setUp(self, points):
        self.polygon = Polygon(points)

if __name__ == "__main__":

    # --------------------------
    # 1 - Polygon object tests
    # --------------------------
    # 1.1 - Union of rectangles with points in all quadrants
    poly_points = [
        (-2, 5),
        (-2, -1),
        (2, -1),
        (2, -4),
        (5, -4),
        (5, 2),
        (1, 2),
        (1, 5),
    ]











    kitchen_points = [
        (1, 1),
        (3, 2),
        (3, 6),
        (1, 5),
    ]

    fridge_points = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1),
    ]

    kitchen = Room("Kitchen", kitchen_points)
    logger.info(kitchen)

    fridge = Furniture("Refrigerator", fridge_points)
    logger.info(fridge)
