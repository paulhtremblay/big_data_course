..  _lesson9_4:

=========================================
Read in a Different File Types
=========================================

Read in a JSON file from disc:

::

 df = spark.read.format("json").load("file:////home/uwadmin/workspace/Spark-The-Definitive-Guide/data/flight-data/json/")
 df.show(2)

Read in a CSV file from disc:

::

 df = spark.read.format("csv")\
 .load("file:////home/uwadmin/workspace/Spark-The-Definitive-Guide/data/flight-data/csv/")

 df.show(1)

Hmm. Not what we wanted. Let's try: 

::

 df = spark.read.format("csv")\
 .options(header = True)\
 .load("file:////home/uwadmin/workspace/Spark-The-Definitive-Guide/data/flight-data/csv/")
 df.show(2)

Ahh, Beauty!


<< :ref:`lesson9_3` | :ref:`lesson9_5`  >>
