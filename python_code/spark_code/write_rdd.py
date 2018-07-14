from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd = sc.textFile('us_stations_90_sample_small.txt')
rdd.saveAsTextFile('file:///tmp/test_out')

