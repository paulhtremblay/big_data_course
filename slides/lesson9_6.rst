..  _lesson9_6:

=========================================
Manipulate Columns
=========================================

Recreate the Data Frame
=======================

::

 df = spark.read.format("json").load("file:////home/uwadmin/workspace/Spark-The-Definitive-Guide/data/flight-data/json/")
 df.printSchema()

Rename a Column
================

::

 df = df.withColumnRenamed("DEST_COUNTRY_NAME", 'destination')
 df.printSchema()

Add a Column
============

:: 

 from pyspark.sql.functions import col, expr
 df = df.withColumn("withinCountry", expr("destination == ORIGIN_COUNTRY_NAME"))
 df.show(2)

Delete a Column
===============

::

 df = df.drop("withinCountry")
 df.printSchema()



<< :ref:`lesson9_5` | :ref:`lesson9_7`  >>
