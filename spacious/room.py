#/usr/bin/env python3

############################
# imports
############################
# standard imports
import sys
from math import sin, cos
import numpy as np

# local imports
from .config import *

def rotate(point, angle, origin=(0, 0)):
    '''
    Rotate a point about another point by given angle in
    radians using the RH rule.
    '''
    # translate vector to origin
    x = point[0] - origin[0]
    y = point[1] - origin[1]
    # multiply by the rotation matrix, then add the offset back in
    new_x = (x * cos(angle) - y * sin(angle)) + origin[0]
    new_y = (x * sin(angle) + y * cos(angle)) + origin[1]
    return new_x, new_y

class Polygon:

    def __init__(self, points):
        '''
        Construct with an ordered list of 2-element tuples of
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
        self.vertices.extend(points)
        self.num_vertices = len(self.vertices)

        # get area and centroid
        self.calc_area()
        self.calc_centroid()

        # create list of segments
        #self.set_segments(points)

    def __str__(self):
        text = "Polygon with vertices:"
        for point in self.vertices:
            text += "\n{}".format(point)
        return text

    def calc_area(self):
        '''
        Calculate the area using the Shoelace Formula.
        '''
        area = 0.0
        for i in range(self.num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % self.num_vertices
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        self.area = abs(area) * 0.5

    def calc_centroid(self):
        '''
        Calculate the centroid or geometric center.
        '''
        c_x = 0.0
        c_y = 0.0
        # get the X coordinate
        for i in range(self.num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % self.num_vertices
            c_x += (self.vertices[i][0] ** 2) * self.vertices[j][1]
            c_x -= self.vertices[i][0] * self.vertices[j][0] * \
                    self.vertices[i][1]
            c_x += self.vertices[i][0] * self.vertices[j][0] * \
                    self.vertices[j][1]
            c_x -= (self.vertices[j][0] ** 2) * self.vertices[i][1]
        c_x *= round(1 / (6 * self.area), 6)
        # get the Y coordinate
        for i in range(self.num_vertices):
            # wrap around to first point at end of list
            j = (i + 1) % self.num_vertices
            c_y += self.vertices[i][0] * self.vertices[i][1] * \
                    self.vertices[j][1]
            c_y -= self.vertices[j][0] * (self.vertices[i][1] ** 2)
            c_y += self.vertices[i][0] * (self.vertices[j][1] ** 2)
            c_y -= self.vertices[j][0] * self.vertices[i][1] * \
                    self.vertices[j][1]
        c_y *= 1 / (6 * self.area)
        self.centroid = (c_x, c_y)

    def rotate(self, angle):
        '''
        Rotate the polygon about the origin by given angle in
        radians using RH rule.
        '''
        rotated_vertices = []
        for point in self.vertices:
            # translate vector to origin
            x = point[0] - self.centroid[0]
            y = point[1] - self.centroid[1]
            new_x = x * cos(angle) - y * sin(angle)
            new_y = x * sin(angle) + y * cos(angle)
            # translate vector back to centroid
            rot_x = new_x + self.centroid[0]
            rot_y = new_y + self.centroid[1]
            rotated_vertices.append((rot_x, rot_y))
        self.vertices = rotated_vertices

    def rotate_np(self, angle):
        '''
        Rotate the polygon about the origin by given angle in
        radians using RH rule.
        '''
        s, c = (np.sin(angle), np.cos(angle))
        r_matrix = np.array([[c, -s], [c, s]])

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

