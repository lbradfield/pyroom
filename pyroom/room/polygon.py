#!/usr/bin/env python3

############################
# Imports
############################
# Standard imports
import sys
from config import *

############################
# Object
############################
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
        from sys import path
        self.vertices = [(0, 0)]
        self.vertices.extend(points)
        self.num_vertices = len(points)

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

    def get_length(self, seg):
        pass

    def get_area(self):
        return self.area

    def calc_area(self):
        '''
        Calculate the area using the Shoelace Formula.
        '''
        area = 0.0
        for i in range(self.num_vertices):
            j = (i + 1) % self.num_vertices
            area += self.vertices[i][0] * self.vertices[j][1]
            area -= self.vertices[j][0] * self.vertices[i][1]
        self.area = abs(area) * 0.5

    def rotate(self, deg):
        '''
        Rotate the polygon about the origin.
        '''

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

