..  _lesson8_4:

=========================================
Creating DataFrames: From RDD 
=========================================

- Often, it is useful to read unstructured data in as an RDD, and then convert it 
  to a dataframe

.. literalinclude:: ../python_code/spark_code/rdd_to_df.py
   :language: python
   :linenos:

`df.columns`
`df.drop('total_variable_characters')`
`df = df.withColumnRenamed('air_temperature_observation_air_temperature', 'temperature')`

- There are many more methods for a dataframe, including groupByKey, withColumn (to add or modify a column),
  join, union, etc.
- We will not cover these methods. Instead, we will convert the dataframe to SQL, and make our transformations there

<< :ref:`lesson8_3` | :ref:`lesson8_5`  >>

