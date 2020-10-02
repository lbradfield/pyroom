#/usr/bin/env python3
print('''
      __file__ = {}
      __name__ = {}
      __package__ = {}
      '''.format(__file__, __name__, __package__))

############################
# imports
############################
# standard imports
import sys
from os.path import abspath, join, dirname

# local imports
import room
from tests import test_room

# add the package to python path temporarily
# TODO: create setup.py to install the package in the standard way
'''
def view_sys_path():
    print('Path:')
    for path in sys.path:
        print(path)
    print('')

print('remove the first item of the path')
sys.path.pop(0)
view_sys_path()
# add this project to the path if it isn't already added
pkg = abspath(join(dirname(__file__), PKG_REL_PATH))
sys.path.insert(0, pkg)
view_sys_path()
'''


if sys.argv[1] == 'test':
    test_room.unittest.main()
