#!/usr/bin/env python
"""mapper.py"""

import sys
import pprint
pp = pprint.PrettyPrinter(indent = 4)

from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict

REGION = 'country'

if REGION == 'country':
    key = 'ctry'
elif REGION == 'state':
    key = 'st'
else:
    raise ValueError("use 'country' or 'st'")

for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue
    the_dict = parse_line(line)
    temp = the_dict['air_temperature_observation_air_temperature']
    region = us_stations_dict.get(str(the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get(key)
    if region == '' or region == None  or temp == None:
        continue
    print('{region}\t{temp}'.format(region = region, temp = temp))
