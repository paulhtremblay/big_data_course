from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([('key1',1), ('key2', 3), ('key1', 2), ('key2', 5)])
rdd2 = rdd1.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())

