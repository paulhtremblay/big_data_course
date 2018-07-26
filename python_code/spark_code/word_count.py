import sys
import os
print(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'copperfield.txt')
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.textFile('file:///{path}'.format(path = path))
rdd2 = rdd1.flatMap(lambda x: x.split(' '))
rdd3 = rdd2.map(lambda x: (x, 1))
rdd4 =  rdd3.reduceByKey(lambda a, b: a + b)


the_list = rdd4.collect()

for i in the_list:
    print(i)



