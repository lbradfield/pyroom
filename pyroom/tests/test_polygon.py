import unittest
from polygon import Polygon

points1 = [(2, 0),
          (2, 3),
          (0, 3),
          ]

points2 = [(1, 3),
          (-2, 2),
          (0, -1.4),
          (8.5, 2)
          ]

class PolygonTestCase(unittest.TestCase):
    def setUp(self):
        self.polygon1 = Polygon(points1)
        self.polygon2 = Polygon(points2)

    def test_str(self):
        self.assertEqual(str(self.polygon1),
                "Polygon with vertices:\n"\
                         "(0, 0)\n"\
                         "(2, 0)\n"\
                         "(2, 3)\n"\
                         "(0, 3)")
        self.assertEqual(str(self.polygon2),
                "Polygon with vertices:\n"\
                         "(0, 0)\n"\
                         "(1, 3)\n"\
                         "(-2, 2)\n"\
                         "(0, -1.4)\n"\
                         "(8.5, 2)")

    def test_calc_area(self):
        self.polygon1.calc_area()
        self.assertEqual(self.polygon1.area, 6.0)

if __name__ == "__main__":
    unittest.main()



