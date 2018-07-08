from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.textFile('copperfield.txt')
rdd2 = rdd1.sample(True, .001)
print(rdd2.count())
