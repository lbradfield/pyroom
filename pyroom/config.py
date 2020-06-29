############################
# imports
############################
import logging

############################
# relative path to package from main.py
############################
PKG_REL_PATH = '..'

############################
# room config
############################
UNITS = 'ft'

############################
# logging setup
############################
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = \
    '%(asctime)s|%(module)s|%(funcName)s|%(levelname)s|%(message)s'
LOG_NAME = 'pyroom'
# create the formatter
formatter = logging.Formatter(LOG_FORMAT)
# create the console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)
# create the logger
logger = logging.getLogger(LOG_NAME)
logger.setLevel(LOG_LEVEL)
# add handlers to the logger
logger.addHandler(console_handler)

