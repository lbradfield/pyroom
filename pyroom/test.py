#!/usr/bin/env python3

############################
# Imports
############################
from room import Room
from furniture import Furniture

if __name__ == "__main__":

    kitchen_points = [
        (1, 1),
        (3, 2),
        (3, 6),
        (1, 5),
    ]

    fridge_points = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1),
    ]

    kitchen = Room("Kitchen", kitchen_points)
    logger.info(kitchen)

    fridge = Furniture("Refrigerator", fridge_points)
    logger.info(fridge)
