from pyspark.sql import SparkSession

from pyspark import SparkContext, SparkConf
from parse_noaa import parse_line
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()
df = spark.read.csv('us_stations_90_sample_small.csv', header=True)
df.show()

