#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
import numpy

import pprint
pp = pprint.PrettyPrinter(indent = 4)

from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict

def find_range(x, edges):
    for i in range(len(edges)):
        if x >= edges[i] and x <= edges[i + 1]:
            return i

with open("../temp_data/stations_avg.txt", 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        values = [float(x[1]) for x in csv_reader]
hist, edges = numpy.histogram(values)

range_dict = {}
with open("../temp_data/stations_avg.txt", 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for line in csv_reader:
            key = line[0]
            value = float(line[1])
            range_dict[key] = find_range(value, edges)



for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue
    the_dict = parse_line(line)
    pp.pprint(the_dict)
    assert False
    temp = the_dict['air_temperature_observation_air_temperature']
    state = us_stations_dict.get(str(
        the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get('st')
    if state == '' or state == None or state == 'AK' or state == 'HI'  or temp == None:
        continue
    print('{state}\t{temp}'.format(state = state, temp = temp))

if __name__ == '__main__':
    print(find_range(27.7))
