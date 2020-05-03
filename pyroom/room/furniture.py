#!/usr/bin/env python3

############################
# Imports
############################
from polygon import Polygon
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
class Furniture(Polygon):
    '''
    Furniture object that interacts with room object.
    '''

    # Get units from config
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
