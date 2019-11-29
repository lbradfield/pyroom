#!/usr/bin/env python3

############################
# Imports
############################
import sys
import logging
#import sympy

import test

############################
# Constants
############################
# Logging
LOG_LEVEL = logging.DEBUG
LOG_NAME = "room"
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
        self.origin = (0,0)

    def get_size(self):
        return self.width, self.depth

    def get_name(self):
        return self.name

    def set_name(self, name):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.name = name

    def set_size(self, width, depth):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.width = width
        self.depth = depth



print(test.test_func())
