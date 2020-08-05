#/usr/bin/env python3

############################
# imports
############################
# standard imports
import sys
from math import sin, cos
import numpy as np

# local imports
from spacious.config import *

class Polygon(object):
    '''
    Base class for room and furniture objects that provides
    mathematical functionality.
    '''

    version = '0.1'

    # precision of floats
    # this is used to convert all floats into ints before
    # calculations take place
    p = 10**7

    def __init__(self, points):
        '''
        Initialize with an ordered list of 2-element tuples of
        integers, which represent points, from which to draw the
        vertices of the polygon.

        Parameters
        ----------
        points : list
            An ordered list of 2-element tuples of integers
            representing points in the polygon, not including the
            origin (0, 0).
        '''
        self.vertices = [(0, 0)]
        self.int_vertices = [(0, 0)]
        for v_x, v_y in points:
            self.vertices.append(
                (v_x, v_y))
            self.int_vertices.append(
                (self.to_int(v_x), self.to_int(v_y)))
        self.num_vertices = len(self.vertices)

        self.set_area()
        self.set_centroid()

    def __str__(self):
        text = "Polygon with vertices:"
        for point in self.vertices:
            text += "\n{}".format(point)
        return text

    @staticmethod
    def to_float(i):
        '''
        '''
        return float(i / Polygon.p)

    @staticmethod
    def to_int(f):
        '''
        '''
        return int(round(f * Polygon.p))

    def set_area(self):
        '''
        Converts float vertices into int vertices by multiplying by
        the precision value before passing to calc_area. Then, return
        value is rounded to nearest 1s place and divided by precision
        value.
        '''
        self.int_area = Polygon.calc_area(self.int_vertices)
        self.area = self.to_float(self.int_area)

    def set_centroid(self):
        '''
        '''
        self.int_centroid = Polygon.calc_centroid(self.int_vertices, self.int_area)
        self.centroid = (
            self.to_float(self.int_centroid[0]),
            self.to_float(self.int_centroid[1]))

    def rotate(self, angle):
        '''
        Rotate the polygon about the centroid by given angle in
        radians using RH rule.
        '''
        rotated_vertices = []
        for vertex in self.vertices:
            rotated_vertices.append(
                rotate_point(vertex, angle, self.centroid))
        self.vertices = rotated_vertices

    @staticmethod
    def calc_area(vertices):
        '''
        Calculate the area of a polygon using the Shoelace Formula
        given the vertices.
        '''
        area = 0.0
        num_vertices = len(vertices)
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        return abs(area) * 0.5

    @staticmethod
    def calc_centroid(vertices, area):
        '''
        Calculate the centroid of a polygon given the vertices and area.
        '''
        c_x = 0.0
        c_y = 0.0
        num_vertices = len(vertices)
        # get the X coordinate
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            c_x += (vertices[i][0] ** 2) * vertices[j][1]
            c_x -= vertices[i][0] * vertices[j][0] * \
                    vertices[i][1]
            c_x += vertices[i][0] * vertices[j][0] * \
                    vertices[j][1]
            c_x -= (vertices[j][0] ** 2) * vertices[i][1]
        c_x *= 1 / (6 * area)
        # get the Y coordinate
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            c_y += vertices[i][0] * vertices[i][1] * \
                    vertices[j][1]
            c_y -= vertices[j][0] * (vertices[i][1] ** 2)
            c_y += vertices[i][0] * (vertices[j][1] ** 2)
            c_y -= vertices[j][0] * vertices[i][1] * \
                    vertices[j][1]
        c_y *= 1 / (6 * area)
        return c_x, c_y

    @staticmethod
    def rotate_point(point, angle, origin=(0, 0)):
        '''
        Rotate a point about any origin by given angle in radians using
        the RH rule.
        '''
        # translate vector to origin
        x = point[0] - origin[0]
        y = point[1] - origin[1]
        # multiply by the rotation matrix, then add the offset back in
        new_x = (x * cos(angle) - y * sin(angle)) + origin[0]
        new_y = (x * sin(angle) + y * cos(angle)) + origin[1]
        return new_x, new_y

    # unused functions below
    # ----------------------

    def get_vertices(self):
        return self.vertices

    def get_area(self):
        return self.area

    def set_segments(self, points):
        '''
        Incomplete and not needed at this time.
        Input segments as an ordered list of points, and output a
        list of lists of tuples, clumping together vertices that are
        adjacent.

        Parameters
        ----------
        points :

        Examples
        --------
            [(0, 1), (0, 4), (
        '''
        pass

    def add_point(self, x, y):
        '''
        Incomplete and not required at this time
        '''
        point = euclid.Point2(x, y)
        if point not in self.points:
            self.points.append(point)


class Furniture(Polygon):
    '''
    Furniture object that interacts with room object.
    '''

    # get units from config
    units = UNITS

    def __init__(self, name, points):
        self.name = name
        Polygon.__init__(points)

    def __str__(self):
        return "{} - {} {}".format(self.name, self.area, self.units)

    def set_wallside(self, seg):
        '''
        Designates a particular segment to be wall-facing.
        '''
        self.wallside = seg


class Room(Polygon):
    '''
    Room object which holds furniture and inherits basic polygon
    properties from the polygon object.
    '''

    # get units from config
    units = UNITS

    def __init__(self, name, points):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.name = name
        Polygon.__init__(points)
        self.furniture = []

    def __str__(self):
        return "{} - {} {}".format(self.name, self.area, self.units)

    def get_name(self):
        return self.name

    def get_furniture(self):
        return self.furniture

    def add_furniture(self, furn, pos=None):
        '''
        Place a furniture object in the room at a position.

        Parameters
        ----------
        furn : object
        '''
        if pos is not None:
            self.furniture.append((furn, pos))
        else:
            self.furniture.append((furn, self.origin))

