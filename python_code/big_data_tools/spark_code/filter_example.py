import os
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'simple_words_count.txt')
rdd1 = sc.textFile('file:///{path}'.format(path = path))
rdd2 = rdd1.filter(lambda x: 'car' in x)
print(rdd2.collect())


