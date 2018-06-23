import os
import sys
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

from parsers.parse_noaa import parse_line
from parsers.stations_us_dict import d as us_stations_dict
from pyspark.sql import SparkSession
from pyspark import SparkContext
from  pyspark.sql import SQLContext
import boto3
import pprint
pp = pprint.PrettyPrinter(indent = 4)



def get_weather_stations(sc, path):
    rdd = sc.textFile('s3a://{path}'.format(path = path))
    the_list = rdd.takeSample(False, 300)
    return the_list


if __name__ == '__main__':
    sc = SparkContext('local')
    with open('../data/us_stations_sample.txt', 'w') as write_obj:
        pass
    with open('../data/us_stations_keys.txt', 'r') as read_obj:
        line = 'init'
        counter = 0
        while line:
            if line.strip() == '':
                continue
            counter += 1
            line = read_obj.readline()
            print(counter, line)
            the_list = get_weather_stations(sc, 'paulhtremblay/{key}'.format(key = line.strip()))
            with open('../data/us_stations_sample.txt', 'a') as write_obj:
                for i in the_list:
                    write_obj.write('{l}\n'.format(l=i))

