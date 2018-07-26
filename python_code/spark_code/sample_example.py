import os
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copperfield.txt')
rdd1 = sc.textFile('file:///{path}'.format(path = path))
rdd2 = rdd1.sample(True, .001)
print(rdd2.count())
