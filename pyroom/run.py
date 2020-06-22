#/usr/bin/env python3

############################
# Imports
############################
# Standard imports
import sys
import os

def view_sys_path():
    print('Path:')
    for path in sys.path:
        print(path)
    print('')

view_sys_path()
# Add this project to the path if it isn't already added
print(os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../'))
view_sys_path()

# Import pyroom
from pyroom.room.room import Room
