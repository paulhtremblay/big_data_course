#!/usr/bin/env python
"""mapper.py"""

import sys
import pprint
pp = pprint.PrettyPrinter(indent = 4)

from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict

for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue
    the_dict = parse_line(line)
    temp = the_dict['air_temperature_observation_air_temperature']
    state = us_stations_dict.get(str(
        the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get('st')
    if state == '' or state == None or state == 'AK' or state == 'HI'  or temp == None:
        continue
    station_id = the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']
    print('{station_id}\t{temp}'.format(station_id = station_id, temp = temp))
