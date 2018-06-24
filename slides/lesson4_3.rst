..  _lesson4_3:

=============
Lesson 4 (3)
=============

Using Map Reduce to find the average tempeartures for each state
================================================================

The mapper
++++++++++

Steps to create a mapper:

1. Read each line from the file
2. Convert the line to a dictionary by using the noaa parser
3. Get 'fixed_weather_station_usaf_master_station_catalog_identifier'. This value will be a number.
4. Use a pre-defined dictionary to convert the number to a US state
5. Print the results

.. literalinclude:: ../python_code/map_reduce/map_noaa_temp_by_state.py
   :language: python
   :linenos:

Questions
=========

1. What is the difference between this example and the word count example?
2. What are the similarities?
