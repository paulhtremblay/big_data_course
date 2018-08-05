
..  _lesson9_5:

=========================================
Create a Schema
=========================================


::

Create a simple dataframe by first creating an RDD and
converting it.

::

 rdd = sc.parallelize([['MA', None, 25], ['NH', 1.2, 33]])
 df = rdd.toDF()
 df.show()

Yuck. 

::

 from pyspark.sql.types import *
 schema = StructType([StructField("state", StringType()),
                     StructField("temperature", FloatType()),
                     StructField("rainfall", IntegerType()),
                    ])
 df = rdd.toDF(schema = schema)
 df.show(2)
 df.printSchema()

Ah, a thing of beauty. 


<< :ref:`lesson9_4` | :ref:`lesson9_6`  >>
