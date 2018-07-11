import datetime
import sys
from parsers.parse_noaa import parse_line
from pyspark.sql import SparkSession
from pyspark import SparkContext
from  pyspark.sql import SQLContext
import stations_us_dict
import pprint
pp = pprint.PrettyPrinter(indent = 4)

def get_us_state(x):
    if stations_us_dict.d.get(x.get('fixed_weather_station_usaf_master_station_catalog_identifier')).get('st') == '':
        return False
    return True

def consecutive_(x):
    l = sorted(x[1], key = lambda x: x[1])
    current = None
    counter = 0
    the_max = 0
    for i in l:
        if i[0] == None:
            continue
        counter += 1
        if not (current == None or float(i[0]) <= current):
            if counter > the_max:
                the_max = counter
            counter = 0
        current = float(i[0])
    return (x[0], the_max)


def consecutive(path):
    sc = SparkContext('local')
    sc.setLogLevel("WARN")
    sqlContext = SQLContext(sc)
    rdd = sc.textFile('file://{path}'.format(path = path))\
       .map(lambda x: parse_line(x))\
       .filter(get_us_state)\
       .filter(lambda x: x.get('point_observation_date_time') > datetime.datetime(1990, 1, 1))\
       .filter(lambda x: x.get('point_observation_date_time') < datetime.datetime(1990, 2, 1))\
       .map(lambda x: ( stations_us_dict.d.get(x.get('fixed_weather_station_usaf_master_station_catalog_identifier')).get('st'),
            (x.get('air_temperature_observation_air_temperature'),
            x.get('point_observation_date_time')
                )))\
       .groupByKey()\
       .map(consecutive_)

    return rdd


if __name__ == '__main__':
    rdd  = consecutive('/home/paul/Documents/projects/big_data_course/workspace/us_stations_90_sample_small.txt')
    pp.pprint(rdd.take(10))
