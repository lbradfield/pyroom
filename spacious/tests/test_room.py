#/usr/bin/env python3

'''
reference on floating-point errors:
https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/#:~:text=The%20idea%20of%20a%20relative,larger%20of%20the%20two%20numbers.

area calculation can be verified here:
https://rechneronline.de/pi/simple-polygon.php
centroid calculation can be verified here:
http://eguruchela.com/math/Calculator/polygon-centroid-point
rotation calculator
https://comnuan.com/cmnn05/cmnn05001/
'''

# standard imports
import unittest
import math

# this package
from spacious.room import Polygon

# rotate angles in radians
ROTATE_ANGLES = [
    0.0 * math.pi,
    0.5 * math.pi,
    -1.7 * math.pi,
    3.5 * math.pi,
]
# ------------------------------------------------------------
# simple test case
# 2x3 rectangle
points1 = [
    (2.0, 0),
    (2, 3),
    (0.0, 3.0),
]
# area
A1 = 6.0
# centroid
C1 = (1.0, 1.5)
# rotated about the angles in ROTATE_ANGLES
P1_ROTATED = [
    # 0 rad
    [(0.0, 0.0), (2.0, 0.0), (2.0, 3.0), (0.0, 3.0)],
    # 0.5*pi rad
    [(2.5, 0.5), (2.5, 2.5), (-0.5, 2.5), (-0.5, 0.5)],
    # -1.7*pi rad
    [(1.6257, -0.1907),
     (2.8013, 1.4273),
     (0.3743, 3.1907),
     (-0.8013, 1.5727)
    ],
    # 3.5*pi rad
    [(-0.5, 2.5),
     (-0.5, 0.5),
     (2.5, 0.5),
     (2.5, 2.5)
    ],
]
# ------------------------------------------------------------
# edge test case 1
# concave polygon using negative numbers, zero, and decimals
points2 = [
    (1, 3.0),
    (-2, 2.0),
    (0, -1.4),
    (8.5, 2)
]
# area
A2 = 11.35
# centroid
#C2 = (1.286, 0.717)
C2 = (1.2856094, 0.7168869)
# rotated about the angles in ROTATE_ANGLES
P2_ROTATED = [
    # 0 rad
    [(0.0, 0.0), (1.0, 3.0), (-2.0, 2.0), (0.0, -1.4), (8.5, 2.0)],
    # 0.5*pi rad
    [(2.0025, -0.5687),
     (-0.9975, 0.4313),
     (0.0025, -2.5687),
     (3.4025, -0.5687),
     (0.0025, 7.9313)
    ],
    # -1.7*pi rad
    [(1.1099, -0.7446),
     (-0.7293, 1.8278),
     (-1.6837, -1.1870),
     (2.2425, -1.5675),
     (4.4881, 7.3076)
    ],
    # 3.5*pi rad
    [(0.5687, 2.0025),
     (3.5687, 1.0025),
     (2.5687, 4.0025),
     (-0.8313, 2.0025),
     (2.5687, -6.4975)
    ],
]
# ------------------------------------------------------------
# edge test case 2
# concave polygon with one 180 deg vertex
points3 = [
    (5, 0),
    (3.5, -6.0),
    (2, -12),
    (-1.8, -5),
    (-6.0, -5)
]
# area
A3 = 56.3
# centroid
C3 = (-0.7771462, 4.3433985)
# rotated about the angles in ROTATE_ANGLES
P3_ROTATED = [
    # 0 rad
    [(0.0, 0.0),
     (5.0, 0.0),
     (3.5, -6.0),
     (2.0, -12.0),
     (-1.8, -5.0),
     (-6.0, -5.0)
    ],
    # 0.5*pi rad
    [(3.5663, 5.1205),
     (3.5663, 10.1205),
     (9.5663, 8.6205),
     (15.5663, 7.1205),
     (8.5663, 3.3205),
     (8.5663, -0.8795)
    ],
    # -1.7*pi rad
    [(3.1935, 2.4191),
     (6.1325, 6.4642),
     (10.1049, 1.7240),
     (14.0773, -3.0163),
     (6.1806, -1.9760),
     (3.7119, -5.3739)
    ],
    # 3.5*pi rad
    [(-5.1205, 3.5663),
     (-5.1205, -1.4337),
     (-11.1205, 0.0663),
     (-17.1205, 1.5663),
     (-10.1205, 5.3663),
     (-10.1205, 9.5663)
    ],
]

class PolygonTestCase(unittest.TestCase):
    def setUp(self):
        self.polygon1 = Polygon(points1)
        self.polygon2 = Polygon(points2)
        self.polygon3 = Polygon(points3)

    def test_str(self):
        self.assertEqual(str(self.polygon1),
                'Polygon with vertices:\n'\
                         '(0.0, 0.0)\n'\
                         '(2.0, 0.0)\n'\
                         '(2.0, 3.0)\n'\
                         '(0.0, 3.0)')
        self.assertEqual(str(self.polygon2),
                'Polygon with vertices:\n'\
                         '(0.0, 0.0)\n'\
                         '(1.0, 3.0)\n'\
                         '(-2.0, 2.0)\n'\
                         '(0.0, -1.4)\n'\
                         '(8.5, 2.0)')
        self.assertEqual(str(self.polygon3),
                'Polygon with vertices:\n'\
                         '(0.0, 0.0)\n'\
                         '(5.0, 0.0)\n'\
                         '(3.5, -6.0)\n'\
                         '(2.0, -12.0)\n'\
                         '(-1.8, -5.0)\n'\
                         '(-6.0, -5.0)')

    def test_set_area(self):
        self.assertEqual(self.polygon1.area, A1)
        self.assertEqual(self.polygon2.area, A2)
        self.assertEqual(self.polygon3.area, A3)

    def test_set_centroid(self):
        self.assertEqual(self.polygon1.centroid, C1)
        self.assertEqual(self.polygon2.centroid, C2)
        self.assertEqual(self.polygon3.centroid, C3)

    def test_rotate(self):
        for i, angle in enumerate(ROTATE_ANGLES):
            with self.subTest(angle=angle):
                self.polygon1.rotate(angle)
                self.polygon2.rotate(angle)
                self.polygon3.rotate(angle)
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



