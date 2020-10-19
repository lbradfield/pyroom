#/usr/bin/env python3
'''
Main objects to be interacted with and manipulated through the UI.
Includes:
    - Polygon: A base object providing all math operations
    - Room: Inherits Polygon and contains instances of Furniture
    - Furniture: Inherits Polygon and interacts with Room
'''
# TODO:
# - Fix Decimal implementation by using local context during
# calcuations (e.g. with decimal.getcontext() = 9)

############################
# imports
############################
# standard imports
import sys
from math import sin, cos

# 3rd party
import numpy as np
from decimal import Decimal, getcontext, localcontext

# local imports
from spacious.config import *

class Polygon(object):
    '''
    Base class for room and furniture objects that provides
    mathematical functionality.
    '''

    version = '0.1'
    # the precision of floats, provided by Decimal
    getcontext().prec = 5

    def __init__(self, points):
        '''
        Initialize with an ordered list of 2-element tuples of
        integers, which represent points, from which to draw the
        vertices of the polygon.

        Parameters
        ----------
        points : list
            An ordered list of 2-element tuples of floats
            representing points in the polygon, not including the
            origin (0, 0).
        '''
        logger.debug('constructing with points: ' \
                     '{}'.format(points))
        self.vertices = [(0.0, 0.0)]
        for v_x, v_y in points:
            self.vertices.append(
                (float(v_x), float(v_y)))
        self.num_vertices = len(self.vertices)

        self.area = self.calc_area(self.vertices)
        signed_area = self.calc_area(self.vertices, True)
        self.centroid = self.calc_centroid(
            self.vertices, signed_area)

    def __str__(self):
        text = "polygon with vertices:"
        for point in self.vertices:
            text += "\n{}".format(point)
        return text

    def rotate(self, angle):
        '''
        Rotate the polygon about the centroid by given angle in
        radians using RH rule.
        '''
        logger.debug(self)
        rotated_vertices = []
        for vertex in self.vertices:
            rotated_vertices.append(
                self.rotate_point(vertex, angle, self.centroid))
        self.vertices = rotated_vertices

    @staticmethod
    def calc_area(vertices, signed=False):
        '''
        Calculate the area of a polygon using the Shoelace
        Formula given the vertices as floats. This method uses the
        decimal library to perform floating-point calculations.
        '''
        logger.debug('vertices: {}, signed: {}'.format(
            vertices, signed))
        area = Decimal()
        num_vertices = len(vertices)
        with localcontext() as ctx:
            # high-precision calculation
            ctx.prec = 16
            for i in range(num_vertices):
                # wrap around to first point at end of list
                j = (i + 1) % num_vertices
                x_0 = Decimal(str(vertices[i][0]))
                y_0 = Decimal(str(vertices[i][1]))
                x_1 = Decimal(str(vertices[j][0]))
                y_1 = Decimal(str(vertices[j][1]))
                area += x_0 * y_1
                area -= x_1 * y_0
            area /= 2
        # round to the global precision
        area = +area
        logger.debug('area: {}'.format(area))
        if signed:
            return float(area)
        else:
            return float(abs(area))

    @staticmethod
    def calc_centroid(vertices, s_area):
        '''
        Calculate the centroid of a polygon given the vertices and
        area as floats. This method uses the decimal library to
        perform floating-point calculations.
        '''
        logger.debug('vertices: {}, s_area: {}'.format(
            vertices, s_area))
        c_x = Decimal()
        c_y = Decimal()
        num_vertices = len(vertices)
        with localcontext() as ctx:
            # high-precision calculation
            ctx.prec = 16
            for i in range(num_vertices):
                # wrap around to first point at end of list
                j = (i + 1) % num_vertices
                x_0 = Decimal(str(vertices[i][0]))
                y_0 = Decimal(str(vertices[i][1]))
                x_1 = Decimal(str(vertices[j][0]))
                y_1 = Decimal(str(vertices[j][1]))
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
            c_x /= 6 * Decimal(str(s_area))
            c_y /= 6 * Decimal(str(s_area))
        c_x = +c_x
        c_y = +c_y
        logger.debug('c_x, c_y after div: {}'.format((c_x, c_y)))
        return float(c_x), float(c_y)

    @staticmethod
    def rotate_point(point, angle, origin=(0, 0)):
        '''
        Rotate a point about any origin, given as a tuple of floats,
        by given angle in radians using the RH rule. This method
        uses the decimal library to perform floating-point
        calculations.
        '''
        logger.debug('point={}, angle={}, origin={}'.format(
            point, angle, origin))
        sin_ang = Decimal(str(sin(angle)))
        cos_ang = Decimal(str(cos(angle)))
        o_x = Decimal(str(origin[0]))
        o_y = Decimal(str(origin[1]))
        # the point relative to the origin
        x = Decimal(str(point[0])) - o_x
        y = Decimal(str(point[1])) - o_y
        #logger.debug('translate vector to origin: {}'.format((x, y)))
        # multiply by the rotation matrix,
        # then add the offset back in
        new_x = (x * cos_ang - y * sin_ang) + o_x
        new_y = (x * sin_ang + y * cos_ang) + o_y
        logger.debug('rotated point: {}'.format(
            (new_x, new_y)))
        return float(new_x), float(new_y)

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

