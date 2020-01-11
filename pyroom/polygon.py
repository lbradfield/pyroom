#!/usr/bin/env python3

############################
# Imports
############################
from config import *

############################
# Set up logging
############################
LOG_NAME = __name__
# Create the formatter
formatter = logging.Formatter(LOG_FORMAT)
# Create the logger
logger = logging.getLogger(LOG_NAME)
logger.setLevel(LOG_LEVEL)
# Create the console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)
# Add handlers to the logger
logger.addHandler(console_handler)

############################
# Object
############################
class Polygon:

    def __init__(self, points):
        '''
        Construct with an ordered list of 2-element tuples of
        integers, which represent points, from which to draw the
        vertices of the polygon.
        '''
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.vertices = points
        self.num_vertices = len(points)

        # Calculate the area
        self.calc_area()

        # Create list of segments
        #self.set_segments(points)

    def __str__(self):
        text = "Polygon with vertices:"
        for point in self.vertices:
            text += "\n{}".format(point)
        return text

    def get_vertices(self):
        return self.vertices

    def get_length(self, p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    def calc_area(self):
        '''
        Calculate the area using the Shoelace Formula.
        '''
        area = 0.0
        for i in self.num_vertices:
            j = (i + 1) % self.num_vertices
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        self.area = abs(area) * 0.5

    def set_segments(self, points):
        '''
        Incomplete and not needed at this time.
        Input segments as an ordered list of points, and output a
        list of lists of tuples, clumping together vertices that are
        adjacent.
        Ex:
            [(0, 1), (0, 4), (
        '''
        pass

    def add_point(self, x, y):
        '''
        Incomplete and not required at this time
        '''
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        point = euclid.Point2(x, y)
        if point not in self.points:
            self.points.append(point)

