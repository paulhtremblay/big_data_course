from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = rdd1.fold(0, lambda x, y: x + y)
print(rdd2)

