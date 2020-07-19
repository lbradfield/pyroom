#/usr/bin/env python3

# area calculation can be verified here:
# https://rechneronline.de/pi/simple-polygon.php
# centroid calculation can be verified here:
# http://eguruchela.com/math/Calculator/polygon-centroid-point

# standard imports
import unittest
import math

# this package
from spacious.room import Polygon

# simple test case
# 2x3 rectangle
points1 = [(2, 0),
          (2, 3),
          (0, 3),
]
# area
A1 = 6.0
# centroid
C1 = (1, 1.5)

# edge test case 1
# concave polygon using negative numbers, zero, and decimals
points2 = [(1, 3),
          (-2, 2),
          (0, -1.4),
          (8.5, 2)
]
# area
A2 = 11.35
# centroid
#C2 = (1.286, 0.717)
C2 = (1.2856093979441998, 0.7168869309838474)

# edge test case 2
# concave polygon with one 180 deg vertex
points3 = [(5, 0),
          (3.5, -6.0),
          (2, -12),
          (-1.8, -5),
          (-6, -5)
]
# area
A3 = 56.3
# centroid
C3 = (-0.7771462403789224, 4.343398460627591)

# rotate angles in radians
ROTATE_ANGLES = [
    0.0 * math.pi,
    0.5 * math.pi,
    -1.7 * math.pi,
    3.5 * math.pi,
]
P1_ROTATED = [
    [(0, 0), (2, 0), (2, 3), (0, 3)],
    [(0, 0), (2, 0), (2, 3), (0, 3)],
    [(0, 0), (2, 0), (2, 3), (0, 3)],
]
P2_ROTATED = [
]
P3_ROTATED = [
]

class PolygonTestCase(unittest.TestCase):
    def setUp(self):
        self.polygon1 = Polygon(points1)
        self.polygon2 = Polygon(points2)
        self.polygon3 = Polygon(points3)

    def test_str(self):
        self.assertEqual(str(self.polygon1),
                'Polygon with vertices:\n'\
                         '(0, 0)\n'\
                         '(2, 0)\n'\
                         '(2, 3)\n'\
                         '(0, 3)')
        self.assertEqual(str(self.polygon2),
                'Polygon with vertices:\n'\
                         '(0, 0)\n'\
                         '(1, 3)\n'\
                         '(-2, 2)\n'\
                         '(0, -1.4)\n'\
                         '(8.5, 2)')
        self.assertEqual(str(self.polygon3),
                'Polygon with vertices:\n'\
                         '(0, 0)\n'\
                         '(5, 0)\n'\
                         '(3.5, -6.0)\n'\
                         '(2, -12)\n'\
                         '(-1.8, -5)\n'\
                         '(-6, -5)')

    def test_calc_area(self):
        self.polygon1.calc_area()
        self.polygon2.calc_area()
        self.polygon3.calc_area()
        self.assertEqual(self.polygon1.area, A1)
        self.assertEqual(self.polygon2.area, A2)
        self.assertEqual(self.polygon3.area, A3)

    def test_calc_centroid(self):
        self.polygon1.calc_centroid()
        self.polygon2.calc_centroid()
        self.polygon3.calc_centroid()
        self.assertEqual(self.polygon1.centroid, C1)
        self.assertEqual(self.polygon2.centroid, C2)
        self.assertEqual(self.polygon3.centroid, C3)

    def test_rotate(self):
        for angle in ANGLES:
            with self.subTest(i=i):
                self.polygon1.rotate(i)
                self.polygon2.rotate(i)
                self.polygon3.rotate(i)
                self.assertEqual(self.polygon1.vertices,
                                 P1_ROTATED[i])
                self.assertEqual(self.polygon2.vertices,
                                 P2_ROTATED[i])
                self.assertEqual(self.polygon3.vertices,
                                 P3_ROTATED[i])

class RoomTestCase(unittest.TestCase):
    pass



if __name__ == "__main__":
    unittest.main()



