..  _lesson7_5:

=========================================
Outputing Contents of an RDD
=========================================

Let's look at :ref:`lesson3_4` again, and get the same results using an RDD in Spark.

- The `collect` action moves data to the driver--your local computer, in many cases
- If there were Petabytes or Terabyes of data, the program would crash


.. literalinclude:: ../python_code/spark_code/write_rdd.py
   :language: python
   :linenos:

- Spark outputs an RDD to *multiple* files, to a directory
- You can control the number of files with `coalesce`
- We will cover more methods of writing when we cover dataframes


1. Why should you generally avoid using `collect`?
2. How many times is the data read and written from disk? How does that differ from the map/reduce job?

Class Exercise
==============
Read in the two texts from Dickens. Count the words. Save the file to Hadoop.


<< :ref:`lesson7_4` | :ref:`lesson7_6`  >>
