..  _lesson7_3:

=========================================
Reading in multiple files
=========================================

- Reading in a single file can take too long
- Usually we will read in multiple files at once. This allows for multi-threading and is very fast
- You only need to put an asterisk (`*`) at the end of the path

`sc.readTextFile('s3a:///data/henry/noaa_samples/*')`

- Reading in compressed files is faster, and is also automatic:


`sc = readTextFile('paulhtremblay/noaa/data/1901/029070-99999-1901.gz')`

or, read in all the compressed files for 1901:

`sc = readTextFile('paulhtremblay/noaa/data/1901/*')`



Questions
=========

1. Why is reading in multiple files faster?
2. Why is reading in compressed files faster (think of the golden rule)? 

<< :ref:`lesson7_2` | :ref:`lesson7_4`  >>
