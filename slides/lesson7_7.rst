..  _lesson7_7:

=====================================================
Getting the Average Temperature Per Country with RDD
=====================================================

.. literalinclude:: ../python_code/spark_code/temp_us_counties.py
   :language: python
   :linenos:


Here is the code to make a geographical map::
 
 import os
 import csv
 from bokeh.palettes import *
 from big_data_tools.bokeh_tools.all_p import *
 counties_dict = {}
 with open('counties_results/part-00000', 'r') as read_obj:
     csv_reader = csv.reader(read_obj)
     for line in csv_reader:
         counties_dict[line[0]] = float(line[1])
 palette = Oranges[9]
 make_us_map(the_type = 'county', default_color="gray", data = counties_dict,
         palette=palette)

Questions
=========

1. What are 3 questions you can think of when you look at the map?
2. Why did we use mapPartition for mapping the counties?

<< :ref:`lesson7_6` | :ref:`lesson7_8`  >>
