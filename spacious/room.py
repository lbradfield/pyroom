#/usr/bin/env python3
# TODO:
'''
'''


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

    # precision - number of decimal places to use in float and integer
    # representation
    prec = 7

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
        logger.debug('')
        logger.debug('constructing with points: ' \
                     '{}'.format(points))
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
        logger.debug('')
        rotated_vertices = []
        for vertex in self.vertices:
            rotated_vertices.append(
                self.rotate_point(vertex, angle, self.centroid))
        self.vertices = rotated_vertices

    @staticmethod
    def to_float(i, power=1):
        '''
        Translate a large integer value into a floating point value
        by dividing by the precision, p.
        '''
        logger.debug('i: {}, power: {}'.format(i, power))
        int_i = int(round(i))
        logger.debug('int_i: {}'.format(int_i))
        raw_f = int_i / (10 ** (Polygon.prec * power))
        logger.debug('raw_f: {}'.format(raw_f))
        # round to 1 less than the precision to handle numbers very
        # close to zero (e.g. -1e-07)
        return float(round(raw_f, Polygon.prec - 1))

    @staticmethod
    def to_int(f, power=1):
        ''' Translate a small floating point value into a large
        integer value by multiplying by the precision, p, and
        rounding to the nearest integer.
        '''
        logger.debug('f: {}, power: {}'.format(f, power))
        big_f = f * (10 ** (Polygon.prec * power))
        logger.debug('big_f: {}'.format(big_f))
        return int(round(big_f))

    @staticmethod
    def calc_area(vertices, signed=False):
        '''
        Calculate the area (float) of a polygon using the Shoelace
        Formula given the vertices as floats. This method transforms
        the floating point vertex values into integers by multiplying
        by the precision, p, performs the calculation, then
        transforms the result back to floating point.
        '''
        logger.debug('vertices: {}, signed: {}'.format(
            vertices, signed))
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
        if signed:
            int_area = area
        else:
            int_area = abs(area)
        # divide by p^2 due to squaring nature of the area
        # calculation
        logger.debug('int_area: {}'.format(int_area))
        return Polygon.to_float(int_area * 0.5, 2)


    @staticmethod
    def calc_centroid(vertices, area):
        '''
        Calculate the centroid of a polygon given the vertices and
        area as integers.
        '''
        logger.debug('vertices: {}, area: {}'.format(
            vertices, area))
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
        logger.debug('transformed c_x, c_y: {}'.format(
            (Polygon.to_float(c_x), Polygon.to_float(c_y))))
        return Polygon.to_float(c_x), Polygon.to_float(c_y)

    #self.rotate_point(vertex, angle, self.centroid))
    @staticmethod
    def rotate_point(point, angle, origin=(0, 0)):
        '''
        Rotate an point about any integer origin by given
        angle in radians (float) using the RH rule.
        '''
        logger.debug('')
        logger.debug('point: {}'.format(point))
        logger.debug('angle: {}'.format(angle))
        logger.debug('origin: {}'.format(origin))
        # transform origin vector elements to ints
        int_origin = (Polygon.to_int(origin[0]),
                      Polygon.to_int(origin[1]))
        logger.debug('int_origin: {}'.format(int_origin))
        # transform the point vector elements to ints,
        # then translate to origin
        x = Polygon.to_int(point[0]) - int_origin[0]
        y = Polygon.to_int(point[1]) - int_origin[1]
        logger.debug('translate vector to origin: {}'.format((x, y)))
        # multiply by the rotation matrix,
        # then add the offset back in
        new_x = (x * cos(angle) - y * sin(angle)) + int_origin[0]
        new_y = (x * sin(angle) + y * cos(angle)) + int_origin[1]
        logger.debug('rotated point: {}'.format(
            (Polygon.to_float(new_x), Polygon.to_float(new_y))))
        return Polygon.to_float(new_x), Polygon.to_float(new_y)

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

