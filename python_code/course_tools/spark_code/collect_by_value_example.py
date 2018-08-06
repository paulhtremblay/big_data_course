from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([('key1',1), ('key2', 3), ('key1', 2), ('key2', 5)])
print(dict(rdd1.countByValue()))

