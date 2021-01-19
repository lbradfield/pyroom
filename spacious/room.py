#/usr/bin/env python3
'''
Main objects to be interacted with and manipulated through the UI.
Includes:
    - Polygon: A base object providing all math operations
    - Room: Inherits Polygon and contains instances of Furniture
    - Furniture: Inherits Polygon and interacts with Room
'''
# TODO:
    # - instantiate mpf numbers with high precision, and only return
    # lower precision numbers

############################
# imports
############################
# standard imports
#import sys

# 3rd party
#import numpy as np
from mpmath import mp, sin, cos

# local imports
from spacious import config

class Polygon(object):
    '''
    Base class for room and furniture objects that provides
    mathematical functionality.
    '''

    version = '0.2'
    dec_places = 20
    #calc_prec = 20

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
        # set the precision
        mp.dps = Polygon.dec_places
        config.logger.debug('constructing with points: '
                            '%s', points)
        #with mp.workdps(Polygon.calc_prec, normalize_output=True):
        self.vertices = [(mp.mpf(), mp.mpf())]
        for v_x, v_y in points:
            rv_x = mp.mpf(str(v_x))
            rv_y = mp.mpf(str(v_y))
            self.vertices.append((rv_x, rv_y))
        self.num_vertices = len(self.vertices)

        self.area, signed_area = self.calc_area(self.vertices)
        self.centroid = self.calc_centroid(
            self.vertices, signed_area)

    def __str__(self):
        text = 'polygon with vertices:'
        for point in self.vertices:
            text += '\n{}'.format(point)
        return text

    def rotate(self, angle):
        '''
        Rotate the polygon about the centroid by given angle in
        radians using RH rule.
        '''
        config.logger.debug(self)
        rotated_vertices = []
        mp_angle = mp.mpf(angle)
        for vertex in self.vertices:
            rotated_vertices.append(
                self.rotate_point(vertex, mp_angle, self.centroid))
        self.vertices = rotated_vertices

    @staticmethod
    def calc_area(vertices):
        '''
        Calculate the area of a polygon using the Shoelace
        Formula given the vertices as floats. This method uses the
        decimal library to perform floating-point calculations.
        '''
        config.logger.debug('vertices: %s', vertices)
        area = mp.mpf()
        num_vertices = len(vertices)
        # high-precision calculation
        #with mp.workdps(Polygon.calc_prec, normalize_output=True):
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            x_0 = vertices[i][0]
            y_0 = vertices[i][1]
            x_1 = vertices[j][0]
            y_1 = vertices[j][1]
            area += x_0 * y_1
            area -= x_1 * y_0
        area /= 2
        config.logger.debug('raw area: %s', area)
        # return a tuple of area and signed area
        return abs(area), area

    @staticmethod
    def calc_centroid(vertices, s_area):
        '''
        Calculate the centroid of a polygon given the vertices and
        area as floats. This method uses the decimal library to
        perform floating-point calculations.
        '''
        config.logger.debug('vertices: %s, s_area: %s',
            vertices, s_area)
        c_x = mp.mpf()
        c_y = mp.mpf()
        num_vertices = len(vertices)
        # high-precision calculation
        #with mp.workdps(Polygon.calc_prec, normalize_output=True):
        for i in range(num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % num_vertices
            x_0 = vertices[i][0]
            y_0 = vertices[i][1]
            x_1 = vertices[j][0]
            y_1 = vertices[j][1]
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
        config.logger.debug('c_x, c_y before div: %s, %s', c_x, c_y)
        c_x /= 6 * s_area
        c_y /= 6 * s_area
        config.logger.debug('c_x, c_y after div: %s, %s', c_x, c_y)
        return c_x, c_y

    @staticmethod
    def rotate_point(point, angle, origin):
        '''
        Rotate a point about any origin, given as a tuple of floats,
        by given angle in radians using the RH rule. This method
        uses the decimal library to perform floating-point
        calculations.
        '''
        config.logger.debug('point=%s, angle=%s, origin=%s',
            point, angle, origin)
        sin_ang = sin(angle)
        cos_ang = cos(angle)
        o_x = origin[0]
        o_y = origin[1]
        # high-precision calculation
        #with mp.workdps(Polygon.calc_prec, normalize_output=True):
        # the point relative to the origin
        x = point[0] - o_x
        y = point[1] - o_y
        #logger.debug('translate vector to origin: {}'.format((x, y)))
        # multiply by the rotation matrix,
        # then add the offset back in
        new_x = (x * cos_ang - y * sin_ang) + o_x
        new_y = (x * sin_ang + y * cos_ang) + o_y
        config.logger.debug('rotated point: %s, %s',
            new_x, new_y)
        return new_x, new_y



class Furniture(Polygon):
    '''
    Furniture object that interacts with room object.
    '''

    # get units from config
    units = config.UNITS

    def __init__(self, name, points):
        self.name = name
        super().__init__(points)

    def __str__(self):
        return '{} - {} {}'.format(self.name, self.area, self.units)

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
    units = config.UNITS

    def __init__(self, name, points):
        self.name = name
        super().__init__(points)
        self.furniture = []

    def __str__(self):
        return '{} - {} {}'.format(self.name, self.area, self.units)

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

