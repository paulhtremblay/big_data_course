from pyspark.sql import SparkSession

from pyspark import SparkContext, SparkConf
from parse_noaa import parse_line
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()
rdd = sc.textFile('us_stations_90s_sample_big.txt')\
    .map(parse_line)
df = rdd.toDF().coalesce(1)
df.write.mode('Overwrite').csv('noaa_as_csv', header=True)
