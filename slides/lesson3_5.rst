..  _lesson3_5:

========================================
Day 3 (5): Simple word count with Hadoop
========================================


First copy the text file to the Hadoop file system:

.. code-block:: bash

  henry@ubuntu:$ bin/hadoop dfs -copyFromLocal data/hadoop_words /user/hduser/hadoop_words
  henry@ubuntu:$ bin/hadoop dfs -ls
  Found 1 items
  drwxr-xr-x   - hduser supergroup          0 2010-05-08 17:40 /user/hduser/hadoop_words
  henry@ubuntu:$ bin/hadoop dfs -ls /user/hduser/hadoop_words

Now run the code:

.. code-block:: bash

  henry@ubuntu$ bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
  -file python_code/mapper.py    -mapper /home/hduser/mapper.py \
  -file python_code/reducer.py   -reducer /home/hduser/reducer.py \
  -input /user/hduser/hadoop_words/* -output /user/hduser/hadoop_words-output

 
Class Exercise
===============

Count the number of words in David Copperfied (found here: http://www.gutenberg.org/files/43111/)
