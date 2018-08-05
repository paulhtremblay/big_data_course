..  _lesson9_8:

=========================================
Writing the resuls
=========================================

CSV
====

Often, the data is so big you want to write it to a file system
like Hadoop or S3. 

::

 df.write\
 .format("csv")\
 .save("file:///home/uwadmin/workspace/tutorial")

Note that the path is a *directory!* Spark will output multiple files 
to this directory.


The above command should have succeeded. Now try it again:

::

 df.write\
 .format("csv")\
 .save("file:///home/uwadmin/workspace/tutorial")

You will get an error because the directory already exists. If you
want to overwrite the contents, use:

::

 df.write\
 .format("csv")\
 .mode("overwrite")\
 .save("file:///home/uwadmin/workspace/tutorial")

Parquet
=======

Parquet is a special file system that is columnar based. It is more effecient to 
read data from this type if your data is wide (has many columns).

::
 
 df.write\
 .mode("overwrite")\
 .format("parquet")\
 .save("file:///home/uwadmin/workspace/tutorial_parquet")

Reading Parquet
---------------

In order to read from a parquet data set, just point the path to the directory.

::

 df = spark.read.format("parquet")\
 .load("file:///home/uwadmin/workspace/tutorial_parquet")
 df.printSchema()

Note how the schema is preserved. This allows you to save your results in an inexpensive 
file system, and preserve the schema as well. 




<< :ref:`lesson9_7`  >>
