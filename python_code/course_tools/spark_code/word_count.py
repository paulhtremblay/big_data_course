import datetime
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
sc.textFile('s3a://paulhtremblay/copperfield.txt')\
    .flatMap(lambda x: x.split(' '))\
    .map(lambda x: (x, 1))\
    .reduceByKey(lambda a, b: a + b)\
    .saveAsTextFile('s3a://paulhtremblay/word_count_output_{date}'.format(date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))



