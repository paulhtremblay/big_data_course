#!/usr/bin/env python

import sys

#This is station, but map/reduce, because reducer will distribute it correctly.
current_station = None
current_station_moisture = 0
current_station_count = 0

def calc_avg(moisture, count):
    if count == 0:
        return 0
    return round(moisture/count,1)

for line in sys.stdin:
    line = line.strip()
    station, moisture = line.split('\t', 1)
    moisture = float(moisture)
    if current_station == station:
        current_station_moisture += moisture
        current_station_count += 1
    else:
        if current_station:
            print('{current_station},{moisture}'.format(
                current_station = current_station,
                moisture = calc_avg(current_station_moisture, current_station_count)))
        current_station_moisture = 0
        current_station = station
        current_station_count = 0

if current_station == station:
    print('{current_station},{moisture}'.format(
                current_station = current_station,
                moisture = calc_avg(current_station_moisture, current_station_count)))
