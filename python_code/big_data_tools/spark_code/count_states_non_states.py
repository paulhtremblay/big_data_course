import sys
from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict
from pyspark.sql import SparkSession
from pyspark import SparkContext
import pprint
pp = pprint.PrettyPrinter(indent = 4)


def add_state(the_dict):
    state = us_stations_dict.get(str(the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get('st')
    country = us_stations_dict.get(str(the_dict['fixed_weather_station_usaf_master_station_catalog_identifier']), {}).get('ctry')
    if state == '':
        state = None
    the_dict['us_state'] = state
    the_dict['country'] = country
    return the_dict

def count_states_non(x):
    if x['us_state'] == '' or x['us_state'] == None:
        return 0
    return 1

def sum_nums(x):
    pass

def count_stations_(path):
    sc = SparkContext('local')
    x = sc.parallelize([1,2,3,4,5,6,7,8,9,10], 2)
    cSum = x.reduce(lambda accum, n: accum + n)
    print(cSum)
    print(x.collect())

def count_stations(path):
    sc = SparkContext('local')
    rdd = sc.textFile(path)\
       .map(lambda x: parse_line(x))\
       .map(lambda x: add_state(x))\
       .map(count_states_non)
    rdd.persist()
    print(rdd.reduce(lambda accum, n: accum + n)/rdd.count())
    return rdd


if __name__ == '__main__':
    rdd = count_stations('../data/us_stations_sample.txt')
