from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from parse_noaa import parse_line

from  pyspark.sql import SQLContext

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()
"""
df = spark.read.csv('us_stations_states.csv', header=True)
df.show()
"""

rdd = sc.textFile('us_stations_90s_sample_big.txt')\
    .map(parse_line)
df = rdd.toDF()
df.registerTempTable('noaa')
max_temp_df = sqlContext.sql("""select max(air_temperature_observation_air_temperature)
    from noaa
    """)
max_temp_df.show()



