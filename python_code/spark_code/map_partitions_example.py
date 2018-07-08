import datetime
import os
from time import sleep
from pyspark import SparkContext, SparkConf


def f(iterator):
    sleep(10)
    for x in iterator:
        yield x.split(' ')

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.textFile('simple_word_count_words.txt')
rdd2 = rdd1.mapPartitions(f)
print(rdd2.collect())



