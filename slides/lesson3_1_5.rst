..  _lesson3_1_5:

===============================
Preliminaries 
===============================

- extract the python 

:: 

 tar -xvzf python_code.tar.gz

- copy files

::

 mkdir -p workspace
 cd workspace
 cp ../python_code/data/simple_words_count.txt .
 cp ../python_code/parsers/parse_noaa.py .
 cp ../python_code/parsers/stations_us_dict.py .
 weget https://s3-us-west-2.amazonaws.com/paulhtremblaypublic/noaa_data/us_stations_90_sample_small.csv
 wget https://s3-us-west-2.amazonaws.com/paulhtremblaypublic/noaa_data/us_stations_90_sample_small.txt
 wget https://s3-us-west-2.amazonaws.com/paulhtremblaypublic/noaa_data/us_stations_90s_sample_big.csv
 wget https://s3-us-west-2.amazonaws.com/paulhtremblaypublic/noaa_data/us_stations_90s_sample_big.txt


<< :ref:`lesson3` | :ref:`lesson3_2`  >>
