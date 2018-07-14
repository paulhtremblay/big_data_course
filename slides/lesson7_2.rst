..  _lesson7_2:

=========================================
File Types
=========================================

- The prefix before a path name shows the file type

`sc.readTextFile('hdfs:///data/henry/noaa_samples/us_stations_90_sample_small.txt')`


The `hdfs` indicates that the file is part of the Hadoop file system

`sc.readTextFile('s3a:///data/henry/noaa_samples/us_stations_90_sample_small.txt')`

The `s3a` indicates an Amazon S3 system

`sc.readTextFile('gs:///data/henry/noaa_samples/us_stations_90_sample_small.txt')`

The `gs` indicates a Google Cloud Platform (GCP) system

`sc.readTextFile('file:///data/henry/noaa_samples/us_stations_90_sample_small.txt')`

the `file` indicates that the file is local, on your hardrive

Questions
=========

1. Why do you think that you *won't* use `file:///` when reading lots of data?
2. What is the slowest part of any data pipeline (transforming data)? 


<< :ref:`lesson7` | :ref:`lesson7_3`  >>
