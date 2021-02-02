# /usr/bin/env python3

# standard imports
import numpy as np
import time

# this package
import spacious.room as room


n_iter = 500
point = (2, 3)
origin = (3, 4)
angle = 1.22173
result = (3.5977, 2.7183)

tot_time = 0.0
for i in range(n_iter):
    start_time = time.time()
    rotated_1 = room.rotate(point, angle, origin)
    tot_time += time.time() - start_time
avg_time_1 = tot_time / n_iter
print("new point 1 = {}".format(rotated_1))
print("rotate without numpy avg runtime\n = {} s".format(avg_time_1))

# TODO: Need to rewrite numpy rotation function
tot_time = 0.0
for i in range(n_iter):
    start_time = time.time()
    rotated_2 = room.rotate_np(point, angle, origin)
    tot_time += time.time() - start_time
avg_time_2 = tot_time / n_iter
print("new point 1 = {}".format(rotated_2))
print("rotate with numpy avg runtime\n = {} s".format(avg_time_2))
