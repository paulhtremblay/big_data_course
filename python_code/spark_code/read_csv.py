from pyspark.sql import SparkSession
spark = SparkSession.builder \
 .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()

rdd = spark.read\
    .option("header", "true")\
    .csv("test.csv").rdd
#         cheating  ^^^^
print(rdd.take(1))
