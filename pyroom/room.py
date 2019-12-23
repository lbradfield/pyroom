#!/usr/bin/env python3

############################
# Imports
############################
import sys
import logging
#import sympy
#from euclid import *
import euclid
import math

import test

############################
# Constants
############################
# Logging
LOG_LEVEL = logging.DEBUG
LOG_NAME = __main__
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

############################
# Setup logging
############################
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
class Room:

    def __init__(self):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.points = []
        self.walls = []
        self.width = None
        self.depth = None

    # TODO: Impliment a room generation based on input width and
    # depth
    # def set_size(self, width, depth):
    #     logger.debug("Func() : " + sys._getframe().f_code.co_name)
    #     self.width = width
    #     self.depth = depth

    def get_size(self):
        return self.width * self.depth

    def get_name(self):
        return self.name

    def get_walls(self):
        return self.walls

    def get_points(self):
        return self.points

    def set_name(self, name):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.name = name

    def add_point(self, x, y):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        point = euclid.Point2(x, y)
        if point not in self.points:
            self.points.append(point)

    # TODO: Add capability to create diagonal walls
    def find_walls(self):
        # Connect points to form walls if the points have either the
        # same X coordinate or the same Y coordinate
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        right_triangles = []
        points_len = len(self.points)
        for i in range(points_len):
            # Compare this point to the rest of the points in the
            # list
            logger.debug("for {}".format(self.points[i]))
            for j in range(i + 1, points_len):
                logger.debug("against {}".format(self.points[j]))
                # If the X coords match or the Y coords match
                if self.points[i].x == self.points[j].x or \
                self.points[i].y == self.points[j].y:
                    # Create a wall from these two points
                    self.add_wall(self.points[i], self.points[j])
                if self.points[i].x == self.points[j].x:
                    # Point j is exactly above or below point i
                    pass
                elif self.points[i].y == self.points[j].y:
                    # Point j is exactly left or right of point i
                    pass

    def find_rectangles_from_points(self):
        rectangles = []
        points_len = len(self.points)
        temp_points = self.points
        for i in range(points_len):
            # Compare this point to the rest of the points in the
            # list
            logger.debug("for {}".format(temp_points[i]))
            group = [temp_points[i]]
            for j in range(i + 1, points_len):
                logger.debug("against {}".format(temp_points[j]))
                if temp_points[i].x == temp_points[j].x:
                    group.append(temp_points[j])

    def find_rectangles_from_walls(self):
        rectangles = []
        temp_walls = self.walls
        walls_len = len(temp_walls)
        for i in range(walls_len):
            right_angle = [temp_walls[i]]
            for j in range(i + 1, walls_len):
                for p in range(2):
                    if temp_walls[j][p] in temp_walls[i]:
                        right_angle.append(temp_walls[j])

    def get_angle(self, wall1, wall2):
        pass

    def get_wall_length(self, wall):
        return math.sqrt((wall[0].x - wall[1].x)**2 + \
                         (wall[0].y - wall[1].y)**2)

    def add_wall(self, point1, point2):
        # Input 2 euclid.Points and create a wall to add to
        # self.walls
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        if self.walls != []:
            for wall in self.walls:
                # If both points in input already comprise an existing
                # wall
                if point1 in wall and point2 in wall:
                    logger.warning("Wall already exists")
                    return
        logger.debug("Adding wall: {}".format((point1,
                                               point2)))
        self.walls.append((point1, point2))

    def find_wall_boxes(self):
        # Search through the walls and find all rectangular areas
        pass


    def get_rectangle_area(self, x_len, y_len):
        return x_len * y_len

    def get_room_area(self):
        pass

    # def get_slope(self, point1, point2):
    #     # Find the slope between two points
    #     logger.debug("Func() : " + sys._getframe().f_code.co_name)
    #     numerator = 

# TODO:
    # 1. Write funct to get rid of wall segments that are in union
    # 2. Write funct to save areas of wall boxes before wall segments
    # are removed



if __name__ == "__main__":
    room = Room()
    room.set_name("Living Room")
    room.add_point(0, 0)
    room.add_point(2, 0)
    room.add_point(2, 2)
    room.add_point(5, 2)
    room.add_point(5, 4)
    room.add_point(0, 4)

    logger.info("Name: {}".format(room.get_name()))
    logger.info("Points: {}".format(room.get_points()))
    room.find_walls()
    logger.info("Wall Coords: {}".format(room.get_walls()))
    logger.info("For wall {}, the length is {}".format(
        room.walls[3], room.get_wall_length(room.walls[3])))
    #logger.info("Size: {} sq ft".format(room.get_size()))

