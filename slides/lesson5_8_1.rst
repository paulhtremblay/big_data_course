..  _lesson5_8_1:

==================================
Executing and examining the Code
==================================

Execute the code in bash::

 cat us_stations_90_sample_small.txt | ./map_noaa_temp_by_station.py |sort | ./reduce_station_temps.py > avg_station_temps.csv

Let's look at the overall distribution::

 with open("avg_station_temps.csv", 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    values = [float(x[1]) for x in csv_reader]
 p = histogram(values)
 show(p)


Let's execute the second step::

 cat us_stations_90_sample_small.txt | ./map_by_temp_range.py | sort | ./reduce_stations_moisture.py  > moisture_by_range.csv

Let's make a bar graph::

 with open("moisture_by_range.csv", 'r') as read_obj:
     csv_reader = csv.reader(read_obj)
     moisture = [(x[0], x[1]) for x in csv_reader]

 def my_sort(x):
    fields = x[0].split("=>")
    return (float(fields[0]), float(fields[1]))

 moisture = sorted(moisture, key = my_sort)
 p = bar(labels=[x[0] for x in moisture], nums = [float(x[1]) for x in moisture], title="Moisture by range")
 p.xaxis.major_label_orientation = "vertical"
 show(p)


<< :ref:`lesson5_8` | :ref:`lesson5_9`  >>


