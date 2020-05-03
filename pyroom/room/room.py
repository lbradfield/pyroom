#/usr/bin/env python3

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
class Room(Polygon):
    '''
    Room object which holds furniture and inherits basic polygon
    properties from the polygon object.
    '''

    # Get units from config
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

    def add_furniture(self, furn, pos=self.origin):
        '''
        Place a furniture object in the room at a position.

        Parameters
        ----------
        furn : object
        '''
        self.furniture.append((furn, pos))



