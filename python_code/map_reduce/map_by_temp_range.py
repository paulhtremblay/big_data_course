#!/usr/bin/env python
"""mapper.py"""

import sys
import csv
import numpy

import pprint
pp = pprint.PrettyPrinter(indent = 4)

from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict


# Get info from file we created in last map/reduct
# This file is small, so we can read it all in on one node
with open("../temp_data/stations_avg.txt", 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        values = [float(x[1]) for x in csv_reader]

# divide the numbers up into ranges. numpy does this nicely!
hist, edges = numpy.histogram(values)

# Let's print out the "edges", or ranges, for later
with open("../temp_data/ranges.csv" , "w") as write_obj:
    for counter, edge in enumerate(list(edges)):
        write_obj.write('{counter},{edge}'.format(
            counter = counter,
            edge = round(edge, 1)))


def find_range(x, edges):
    for i in range(len(edges)):
        if x >= edges[i] and x <= edges[i + 1]:
            return '{start} => {end}'.format(
                    start = str(round(edges[i],1)),
                    end = str(round(edges[i + 1],1)))

# create a range dict for each station
range_dict = {}
with open("../temp_data/stations_avg.txt", 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for line in csv_reader:
            key = line[0]
            value = float(line[1])
            range_dict[key] = find_range(value, edges)

"""
range_dict = {
    '747750': '18.8 => 23.3',
    '747770': '18.8 => 23.3',
    '747804': '18.8 => 23.3',
    '747810': '18.8 => 23.3',
    '747880': '23.3 => 27.7',
    '747900': '14.4 => 18.8',
    ....
}

"""
#END OF PRELIMINARTY CODE (done just once)

for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue
    the_dict = parse_line(line)
    moisture = the_dict['liquid_precipitation_depth_dimension']
    if moisture == None or moisture == 0:
        continue
    the_id = range_dict.get(the_dict['fixed_weather_station_usaf_master_station_catalog_identifier'])
    if the_id == None:
        continue
    print('{the_id}\t{moisture}'.format(the_id = the_id, moisture = moisture))

