import os
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
from parse_noaa import parse_line
from stations_us_dict import d

def add_state(the_dict):
    state = d.get(str(the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get('st')
    if state == '':
        state = None
    the_dict['us_state'] = state
    return the_dict

def get_avg(a, b):
    return (a[0] + b[0], a[1] + b[1])

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'us_stations_90_sample_small.txt')
rdd = sc.textFile('file://{path}'.format(path = path))\
    .map(parse_line)\
       .map(add_state)\
       .filter(lambda x: x.get('us_state') != None)\
       .filter(lambda x: x.get('air_temperature_observation_air_temperature') != None)\
       .map(lambda x: (x.get('us_state'), (x.get('air_temperature_observation_air_temperature'),1)))\
       .reduceByKey(get_avg)\
       .map(lambda x: (x[0], x[1][0]/x[1][1]))\
       .map(lambda x: '{us_state},{temp}'.format(us_state = x[0], temp = x[1]))\
       .coalesce(1)\
       .saveAsTextFile('states_results')




