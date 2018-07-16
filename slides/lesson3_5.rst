..  _lesson3_5:

========================================
Simple word count with Hadoop
========================================


First copy the text file to the Hadoop file system:

.. code-block:: bash

  mkdir workspace
  hdfs dfs -mkdir usr
  hdfs dfs -mkdir usr/hduser
  hdfs dfs -copyFromLocal simple_words.txt usr/hduser/simple_words
  hdfs dfs -ls usr/hduser
  >>Found 1 items
  >>-rw-r--r--   1 uwadmin hadoop         44 2018-07-01 01:29 usr/hduser/simple_words



Now run the code:

.. code-block:: bash

 hadoop jar /opt/hadoop/hadoop-2.7.4/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar \
 -file mapper.py    -mapper mapper.py \
 -file reducer.py   -reducer reducer.py \
 -input usr/hduser/simple_words* -output usr/hduser/simple-words-output

 hdfs dfs -ls usr/hduser/simple-words-output
 hdfs dfs -cat usr/hduser/simple-words-output/part-00000


 
Class Exercise
===============

Count the number of words in David Copperfied (found here: http://www.gutenberg.org/files/43111/)

<< :ref:`lesson3_4` | :ref:`lesson4`  >>
