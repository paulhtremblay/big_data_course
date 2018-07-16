..  _lesson4_5:


=============================================
Creating a Geographical Map from our Results
=============================================

Jupyter
+++++++++++

Start Jupyter

::

 cd ~/workspace
 jupyter notebook

Let's execute this code within Jupyter

::

 from big_data_tools.bokeh_tools.all_p import *
 import csv

 state_dict = {}
 with open("avg_state_temps.csv", 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for line in csv_reader:
        state_dict[line[0]] = float(line[1])
 from bokeh.palettes import *
 make_us_map(the_type = 'state', default_color="blue", data = state_dict,  palette=Oranges[9])

- Jupyter is lets you get results very quickly, and lets you experiment
- It is not meant for production work--for example, building a website or
  creating a weekly report


Questions
=========

1. What did you like most about Jupyter?
1. What did you like least about Jupyter?

<< :ref:`lesson4_4` | :ref:`lesson5_intro`  >>
