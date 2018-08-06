..  _lesson9_7:

=========================================
Using SQL in Spark
=========================================



Import the library:

::

 from  pyspark.sql import SQLContext


Create a sqlContext:

::

 sqlContext = SQLContext(sc)

Create the Data Frame again:

::

 df = spark.read.format("json").load("file:////home/uwadmin/workspace/Spark-The-Definitive-Guide/data/flight-data/json/")

::

Execute SQL

::

 df.registerTempTable('my_table')
 df_sample = sqlContext.sql("""select * from my_table limit 2""")
 df_sample.show(2)


<< :ref:`lesson9_6` | :ref:`lesson9_8`  >>
