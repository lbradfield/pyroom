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
        self.vertices = [(0.0, 0.0)]
        self.int_vertices = [(0, 0)]
        for v_x, v_y in points:
            self.vertices.append(
                (float(v_x), float(v_y)))
            self.int_vertices.append(
                (self.to_int(v_x), self.to_int(v_y)))
        self.num_vertices = len(self.vertices)

        self.area = self.calc_area(self.vertices)
        signed_area = self.calc_area(self.vertices, True)
        self.centroid = self.calc_centroid(
            self.vertices, signed_area)

    def __str__(self):
        text = "Polygon with vertices:"
        for point in self.vertices:
            text += "\n{}".format(point)
        return text

    def rotate(self, angle):
        '''
        Rotate the polygon about the centroid by given angle in
        radians using RH rule.
        '''
        rotated_vertices = []
        for int_vertex in self.int_vertices:
            rotated_vertices.append(
                self.rotate_point(int_vertex, angle, self.int_centroid))
        self.int_vertices = rotated_vertices

    @staticmethod
    def to_float(i, power=1):
        '''
        Translate a large integer value into a floating point value
        by dividing by the precision, p.
        '''
        int_i = int(round(i))
        return float(int_i / (Polygon.p ** power))

    @staticmethod
    def to_int(f, power=1):
        '''
        Translate a small floating point value into a large integer
        value by multiplying by the precision, p, and rounding to the
        nearest integer.
        '''
        big_f = f * (Polygon.p ** power)
        return int(round(big_f))

    @staticmethod
    def calc_area(vertices, signed=False):
        '''
        Calculate the area (float) of a polygon using the Shoelace
        Formula given the vertices as floats. This method translates
        the floating point vertex values into integers by multiplying
        by the precision, p, performs the calculation, then
        translates the result back to floating point.
        '''
        area = 0
        num_vertices = len(vertices)
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            x_0 = Polygon.to_int(vertices[i][0])
            y_0 = Polygon.to_int(vertices[i][1])
            x_1 = Polygon.to_int(vertices[j][0])
            y_1 = Polygon.to_int(vertices[j][1])
            area += x_0 * y_1
            area -= x_1 * y_0
        # divide by p^2 due to squaring nature of the area
        # calculation
        if signed:
            return Polygon.to_float(area * 0.5, 2)
        else:
            return Polygon.to_float(abs(area) * 0.5, 2)

    @staticmethod
    def calc_centroid(vertices, area):
        '''
        Calculate the centroid of a polygon given the vertices and
        area as integers.
        '''
        logger.debug('Func: ' \
                     '{}'.format(sys._getframe().f_code.co_name))
        c_x = 0
        c_y = 0
        num_vertices = len(vertices)
        signed_int_area = Polygon.to_int(area, 2)
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            x_0 = Polygon.to_int(vertices[i][0])
            y_0 = Polygon.to_int(vertices[i][1])
            x_1 = Polygon.to_int(vertices[j][0])
            y_1 = Polygon.to_int(vertices[j][1])
            # get the X coordinate
            c_x += (x_0 ** 2) * y_1
            c_x -= x_0 * x_1 * y_0
            c_x += x_0 * x_1 * y_1
            c_x -= (x_1 ** 2) * y_0
            # get the Y coordinate
            c_y += x_0 * y_0 * y_1
            c_y -= x_1 * (y_0 ** 2)
            c_y += x_0 * (y_1 ** 2)
            c_y -= x_1 * y_0 * y_1
        logger.debug('c_x, c_y before div: {}'.format((c_x, c_y)))
        c_x *= 1 / (6 * signed_int_area)
        c_y *= 1 / (6 * signed_int_area)
        logger.debug('c_x, c_y after div: {}'.format((c_x, c_y)))
        logger.debug('translated c_x, c_y: {}'.format(
            (Polygon.to_float(c_x), Polygon.to_float(c_y))))
        return Polygon.to_float(c_x), Polygon.to_float(c_y)

    @staticmethod
    def rotate_point(point, angle, origin=(0, 0)):
        '''
        Rotate an point about any integer origin by given
        angle in radians (float) using the RH rule.
        '''
        logger.debug('Func: ' \
                     '{}'.format(sys._getframe().f_code.co_name))
        logger.debug('point: {}'.format(point))
        logger.debug('angle: {}'.format(angle))
        logger.debug('origin: {}'.format(origin))
        # translate vector to origin
        x = point[0] - origin[0]
        y = point[1] - origin[1]
        logger.debug('translate vector to origin: {}'.format((x, y)))
        # multiply by the rotation matrix, then add the offset back in
        new_x = (x * cos(angle) - y * sin(angle)) + origin[0]
        new_y = (x * sin(angle) + y * cos(angle)) + origin[1]
        logger.debug('rotated point: {}'.format(
            (int(round(new_x)), int(round(new_y)))))
        return int(round(new_x)), int(round(new_y))

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

