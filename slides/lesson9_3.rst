..  _lesson9_3:

=========================================
Install the correct Libraries
=========================================

Import the libraries

::

 from pyspark import SparkContext, SparkConf
 from pyspark.sql import SparkSession


Create an RDD and test:

::
 conf = SparkConf().setAppName('Summer_Course').setMaster('local')
 sc = SparkContext(conf=conf)
 rdd_test = sc.parallelize([1,2, 3])
 rdd_test.take(1)

Create a Data Frame and test:


::

 spark = SparkSession.builder\
  .master("local") \
 .appName("Summer_Course") \
 .getOrCreate()
 df = spark.range(500).toDF("number")
 df.show(2)

<< :ref:`lesson9_2` | :ref:`lesson9_4`  >>
