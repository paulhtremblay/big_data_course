..  _lesson7_5:

=========================================
Outputing Contents of an RDD
=========================================


- Inefficient and often impossible to collect data.

Look at lesson 3: :ref:`lesson3_3` 

- Spark outputs an RDD to *multiple* files, to a directory
- You can control the number of files with `coalesce`
- We will cover more methods of writing when we cover dataframes

.. literalinclude:: ../python_code/spark_code/write_rdd.py
   :language: python
   :linenos:



Questions
=========

1. Why should you generally avoid using `collect`?

Class Exercise
==============

Read in the two texts from Dickens. Count the words. Save the file to Hadoop.


<< :ref:`lesson7_4` | :ref:`lesson7_6`  >>
