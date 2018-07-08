import sys
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.textFile('copperfield.txt')
rdd2 = rdd1.flatMap(lambda x: x.split(' '))
rdd3 = rdd2.map(lambda x: (x, 1))
rdd4 =  reduceByKey(lambda a, b: a + b)

the_list = rdd2.collect()

for i in the_list:
    print(i)



