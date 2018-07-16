..  _lesson8_3:

=========================================
Creating DataFrames: CSV
=========================================

- A very common way to create a dataframe in Spark is to read it in directly 
  from a file. Spark can read CSV, JSON, Parquet, and ARVO formats, amongst others.
  We will read in a file from CSV.

.. literalinclude:: ../python_code/spark_code/read_csv_df.py
   :language: python
   :linenos:

To read in a JSON file, you would use::

 df = spark.read.json('us_stations_90_sample_small.json')

For a parquet file::

 df = spark.read.parquet('us_stations_90_sample_small.parquet')

In our example, we read in one file. It is more common to read in files from a directory. 
In that case, use a directory for your argument::

 df = spark.read.json('csv_files_directory')

<< :ref:`lesson8_2` | :ref:`lesson8_4`  >>
