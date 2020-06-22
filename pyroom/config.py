############################
# Imports
############################
import logging

############################
# room config
############################
UNITS = 'ft'

############################
# Logging setup
############################
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = \
    '%(asctime)s|%(module)s|%(funcName)s|%(levelname)s|%(message)s'
LOG_NAME = 'pyroom'
# Create the formatter
formatter = logging.Formatter(LOG_FORMAT)
# Create the console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)
# Create the logger
logger = logging.getLogger(LOG_NAME)
logger.setLevel(LOG_LEVEL)
# Add handlers to the logger
logger.addHandler(console_handler)

