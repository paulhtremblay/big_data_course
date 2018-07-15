import os
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
from parse_noaa import parse_line
from stations_us_dict import d
from big_data_tools.bokeh_tools.choropleth_prep import Chorpleth

import pprint
pp = pprint.PrettyPrinter(indent = 4)

def add_state(the_dict):
    state = d.get(str(the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get('st')
    if state == '' or state  in ['AK', 'HI'] :
        state = None
    the_dict['us_state'] = state
    return the_dict

def get_county(iterator):

    choropleth = Chorpleth(the_type = 'county')
    for the_tuple in iterator:
        county = choropleth.get_id_of_shape((the_tuple[1],the_tuple[2]))
        yield (the_tuple[0], county)

#INEFFICIENT
def get_county_(the_dict):
    choropleth = Chorpleth(the_type = 'county')
    the_dict['county'] = choropleth.get_id_of_shape((the_dict.get('geophysical_point_observation_longitude_coordinate'),
        the_dict.get('geophysical_point_observation_latitude_coordinate')))
    return the_dict

def get_avg(a, b):
    return (a[0] + b[0], a[1] + b[1])

def map_county(the_dict, counties_dict):
    the_dict['county'] = counties_dict.get(the_dict.get('fixed_weather_station_usaf_master_station_catalog_identifier'))
    return the_dict

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'us_stations_90_sample_small.txt')
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'us_stations_90s_sample_big.txt')
rdd1 = sc.textFile('file://{path}'.format(path = path))\
    .map(parse_line)\
       .map(add_state)\
       .filter(lambda x: x.get('us_state') != None)\
       .filter(lambda x: x.get('air_temperature_observation_air_temperature') != None)\
       .persist()
rdd2 = rdd1.map(lambda x: (x.get('fixed_weather_station_usaf_master_station_catalog_identifier'),
            x.get('geophysical_point_observation_longitude_coordinate'),
            x.get('geophysical_point_observation_latitude_coordinate')
        ))\
        .distinct()\
        .mapPartitions(get_county)
counties_dict = {}
for i in rdd2.collect():
    counties_dict[i[0]] = i[1]

rdd3 = rdd1.map(lambda x: map_county(x, counties_dict))\
        .filter(lambda x: x.get('county') != None)\
       .map(lambda x: (x.get('county'), (x.get('air_temperature_observation_air_temperature'),1)))\
       .reduceByKey(get_avg)\
       .map(lambda x: (x[0], x[1][0]/x[1][1]))\
       .map(lambda x: '{county},{temp}'.format(county = x[0], temp = x[1]))\
       .coalesce(1)\
       .saveAsTextFile('counties_results')

