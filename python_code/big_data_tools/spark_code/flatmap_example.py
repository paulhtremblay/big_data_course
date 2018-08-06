from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Summer_Course').setMaster('local')
sc = SparkContext(conf=conf)
rdd1 = sc.textFile('simple_word_count_words.txt')
rdd2 = rdd1.flatMap(lambda x: x.split(' '))
print(rdd2.collect())


