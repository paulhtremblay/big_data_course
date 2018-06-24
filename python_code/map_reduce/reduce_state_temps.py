#!/usr/bin/env python

import sys

#This is state, but map/reduce, because reducer will distribute it correctly.
current_state = None
current_state_count = 0
current_state_temp = 0

def calc_avg(temp, count):
    if count == 0:
        return 0
    return round(temp/count,1)

for line in sys.stdin:
    line = line.strip()
    state, temp = line.split('\t', 1)
    temp = float(temp)
    if current_state == state:
        current_state_temp += temp
        current_state_count += 1
    else:
        if current_state:
            print('{current_state},{avg}'.format(
                current_state = current_state,
                avg = calc_avg(current_state_temp,current_state_count)))
        current_state_count = 0
        current_state_temp = 0
        current_state = state

if current_state == state:
    print('{current_state},{avg}'.format(
                current_state = current_state,
                avg = calc_avg(current_state_temp,current_state_count)))
