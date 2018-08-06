from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark import SparkContext, SparkConf
from parse_noaa import parse_line
from parse_noaa import parse_line

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()
rdd = sc.textFile('us_stations_90_sample_small.txt')\
    .map(parse_line)
df = rdd.toDF()
df.show()

