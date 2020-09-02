#/usr/bin/env python3

'''
reference on floating-point errors:
https://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/#:~:text=The%20idea%20of%20a%20relative,larger%20of%20the%20two%20numbers.

interactive polygon plotter
https://www.mathsisfun.com/geometry/polygons-interactive.html
area calculation can be verified here:
https://rechneronline.de/pi/simple-polygon.php
centroid calculation can be verified here:
http://eguruchela.com/math/Calculator/polygon-centroid-point
rotation calculator
https://comnuan.com/cmnn05/cmnn05001/
'''

# TODO: Add test case for triangle to catch signed vs unsigned area
# in centroid calculation

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
# vertices
V1 = [
    (0.0, 0.0),
    (2.0, 0.0),
    (2.0, 3.0),
    (0.0, 3.0),
]
# area
A1 = 6.0
# signed area, used for centroid calculation
SA1 = 0
# centroid
C1 = (1.0, 1.5)
# rotated about the angles in ROTATE_ANGLES
P1_ROTATED = [
    # 0 rad
    [(0.0, 0.0), (2.0, 0.0), (2.0, 3.0), (0.0, 3.0)],
    # 0.5*pi rad
    [(2.5, 0.5), (2.5, 2.5), (-0.5, 2.5), (-0.5, 0.5)],
    # -1.7*pi rad
    [(1.6257402, -0.1906949),
     (2.8013107, 1.4273391),
     (0.3742598, 3.1906949),
     (-0.8013107, 1.5726609)
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
# vertices
V2 = [
    (0.0, 0.0),
    (1.0, 3.0),
    (-2.0, 2.0),
    (0.0, -1.4),
    (8.5, 2.0)
]
# area
A2 = 11.35
# signed area, used for centroid calculation
SA2 = 0
# centroid
C2 = (1.2856094, 0.7168869)
# rotated about the angles in ROTATE_ANGLES
P2_ROTATED = [
    # 0 rad
    [(0.0, 0.0), (1.0, 3.0), (-2.0, 2.0), (0.0, -1.4), (8.5, 2.0)],
    # 0.5*pi rad
    [(2.0024963, -0.5687225),
     (-0.9975037, 0.4312775),
     (0.0024963, -2.5687225),
     (3.4024963, -0.5687225),
     (0.0024963, 7.9312775)
    ],
    # -1.7*pi rad
    [(1.1099208, -0.7445685),
     (-0.7293449, 1.8278043),
     (-1.6836837, -1.1870320),
     (2.2425446, -1.5674679),
     (4.4880615, 7.3076465)
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
# vertices
V3 = [
    (0.0, 0.0),
    (5.0, 0.0),
    (3.5, -6.0),
    (2.0, -12.0),
    (-1.8, -5.0),
    (-6.0, -5.0)
]
# area
A3 = 56.3
# signed area, used for centroid calculation
SA3 = 0
# centroid
C3 = (0.7771462, -4.3433985)
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
    [(-3.5662523, -5.1205447),
     (-3.5662523, -0.1205447),
     (2.4337477, -1.6205447),
     (8.4337477, -3.1205447),
     (1.4337477, -6.9205447),
     (1.4337477, -11.1205447),
    ],
    # -1.7*pi rad
    [(-3.1935321, -2.4191374),
     (-0.2546058, 1.6259476),
     (3.7178183, -3.1142894),
     (7.6902424, -7.8545264),
     (-0.2064606, -6.8142943),
     (-2.6751586, -10.2121656),
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
        print('start')
        self.polygon1 = Polygon(points1)
        print('p1')
        self.polygon2 = Polygon(points2)
        print('p2')
        self.polygon3 = Polygon(points3)
        print('p3')

    def test_vertices(self):
        print('vertex')
        self.assertEqual(self.polygon1.vertices, V1)
        print('v1')
        self.assertEqual(self.polygon2.vertices, V2)
        print('v2')
        self.assertEqual(self.polygon3.vertices, V3)
        print('v3')

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

    def test_area_unsigned(self):
        self.assertEqual(self.polygon1.area, A1)
        self.assertEqual(self.polygon2.area, A2)
        self.assertEqual(self.polygon3.area, A3)

    def test_area_signed(self):
        self.assertEqual(self.polygon1.calc_area(
            self.polygon1.vertices, True), SA1)
        self.assertEqual(self.polygon2.calc_area(
            self.polygon2.vertices, True), SA2)
        self.assertEqual(self.polygon3.calc_area(
            self.polygon3.vertices, True), SA3)

    def test_centroid(self):
        self.assertEqual(self.polygon1.centroid, C1)
        self.assertEqual(self.polygon2.centroid, C2)
        self.assertEqual(self.polygon3.centroid, C3)

    def test_rotate_point(self):
        for i, angle in enumerate(ROTATE_ANGLES):
            with self.subTest(angle=angle):
                for j in range(len(V1)):
                    self.assertEqual(
                        Polygon.rotate_point(V1[j], angle, C1),
                            P1_ROTATED[j])
                for j in range(len(V2)):
                    self.assertEqual(
                        Polygon.rotate_point(V2[j], angle, C2),
                            P1_ROTATED[j])
                for j in range(len(V3)):
                    self.assertEqual(
                        Polygon.rotate_point(V3[j], angle, C3),
                            P1_ROTATED[j])

    def test_rotate(self):
        for i, angle in enumerate(ROTATE_ANGLES):
            with self.subTest(angle=angle):
                self.polygon1.rotate(angle)
                self.polygon2.rotate(angle)
                self.polygon3.rotate(angle)
                print(angle)
                print(-angle)
                print(self.polygon1.vertices)
                print(P1_ROTATED[i])
                self.assertEqual(self.polygon1.vertices,
                                 P1_ROTATED[i])
                self.assertEqual(self.polygon2.vertices,
                                 P2_ROTATED[i])
                self.assertEqual(self.polygon3.vertices,
                                 P3_ROTATED[i])
            self.polygon1.rotate(-angle)
            self.polygon2.rotate(-angle)
            self.polygon3.rotate(-angle)
            self.assertEqual(self.polygon1.vertices, V1)
            self.assertEqual(self.polygon2.vertices, V2)
            self.assertEqual(self.polygon3.vertices, V3)
            print(self.polygon1.vertices)

class RoomTestCase(unittest.TestCase):
    pass



if __name__ == "__main__":
    unittest.main()



