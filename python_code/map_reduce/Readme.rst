cat ../data/simple_work_count_words.txt | ./mapper.py | sort | ./reducer.py

For by state ananysis
=======================
1. to run::

 cat us_stations_90_sample_small.txt |./map_noaa_temp_by_state.py | sort | ./reduce_state_temps.py > avg_state_temps.csv

2. To get results (in Jupyter)::
 from big_data_tools.bokeh_tools.all_p import *
 import csv

 state_dict = {}
 with open("temp_data/avg_state_temps.csv", 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for line in csv_reader:
        state_dict[line[0]] = float(line[1])
 from bokeh.palettes import *
 make_us_map(the_type = 'state', default_color="blue", data = state_dict,  palette=Oranges[9])



For Range analysis
==================
::
 cat us_stations_90_sample_small.txt | ./map_noaa_temp_by_station.py |sort | ./reduce_station_temps.py > avg_station_temps.csv

::
 with open("avg_station_temps.csv", 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    values = [float(x[1]) for x in csv_reader]

.. comment

::
 cat us_stations_90_sample_small.txt | ./map_by_temp_range.py | sort | ./reduce_stations_moisture.py  > moisture_by_range.csv

 with open("moisture_by_range.csv", 'r') as read_obj:
     csv_reader = csv.reader(read_obj)
     moisture = [(x[0], x[1]) for x in csv_reader]

 def my_sort(x):
    fields = x[0].split("=>")
    return (float(fields[0]), float(fields[1]))

 moisture = sorted(moisture, key = my_sort)
 p = bar(labels=[x[0] for x in moisture], nums = [float(x[1]) for x in moisture])

For Hadoop
==========
