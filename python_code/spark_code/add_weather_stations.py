import sys
from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict
from pyspark.sql import SparkSession
from pyspark import SparkContext
from  pyspark.sql import SQLContext
import boto3
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

def get_weather_stations(path):
    sc = SparkContext('local')
    sqlContext = SQLContext(sc)
    rdd = sc.textFile('s3a://{path}'.format(path = path))\
       .map(lambda x: parse_line(x))\
       .map(lambda x: add_state(x))\
       .filter(lambda x: x.get('country') == 'US')\
       .filter(lambda x: x.get('us_state') != None )
    return rdd


if __name__ == '__main__':
    #rdd  = get_weather_stations('paulhtremblay/noaa/data/1901/029070-99999-1901.gz')
    rdd  = get_weather_stations('paulhtremblay/noaa/data/2000')
    #rdd  = get_weather_stations('paulhtremblay/noaa/data/1930')
    pp.pprint(rdd.take(1))
    #df =  get_weather_stations('paulhtremblay/noaa/data/1901/029070-99999-1901.gz')
    #df =  get_weather_stations('paulhtremblay/noaa/data/1930')
    #print(df.collect())
