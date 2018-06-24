#!/usr/bin/env python

import sys

#This is stations, but map/reduce, because reducer will distribute it correctly.
current_stations = None
current_stations_count = 0
current_stations_temp = 0

def calc_avg(temp, count):
    if count == 0:
        return 0
    return round(temp/count,1)

for line in sys.stdin:
    line = line.strip()
    stations, temp = line.split('\t', 1)
    temp = float(temp)
    if current_stations == stations:
        current_stations_temp += temp
        current_stations_count += 1
    else:
        if current_stations:
            print('{current_stations},{avg}'.format(
                current_stations = current_stations,
                avg = calc_avg(current_stations_temp,current_stations_count)))
        current_stations_count = 0
        current_stations_temp = 0
        current_stations = stations

if current_stations == stations:
    print('{current_stations},{avg}'.format(
                current_stations = current_stations,
                avg = calc_avg(current_stations_temp,current_stations_count)))
