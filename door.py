#!/usr/bin/env python3

############################
# Imports
############################
import sys
import logging


############################
# Constants
############################
# Logging
LOG_LEVEL = logging.DEBUG
LOG_NAME = "door"
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
class Door:

    def __init__(self):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)

    def get_length(self):
        return self.length

    def set_length(self, length):
        logger.debug("Func() : " + sys._getframe().f_code.co_name)
        self.length = length

