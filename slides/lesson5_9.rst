..  _lesson5_9:

================================
Summary Map Reduce
================================

Agenda
------------

Learn that THE SLOWEST PART OF JOBS IN BIG DATA IS INPUT/OUTPUT!


History
-------

- 2004, Google developed a proprietary project, solving 3 problems:


The three main problems solved were:

1. Parallelization: how to parallelize the computation
2. Distribution: how to distribute the data
3. Fault-tolerance: how to handle component failure

- 2006, Hadoop makes map/reduce widely available. 
- Facebook and others begin using it

.. Spark, 2009

Advantages
------------

- scalable, 
- able to work with unstructured code
- able to work on commodity (cheap) machines 
- *relatively* easy to write jobs (as opposed to previously)
   


Disadvantages
---------------

- difficult to write complex jobs
- difficult to write jobs with multi steps
- inefficient for jobs with multiple steps
- THE SLOWEST PART OF JOBS IN BIG DATA IS INPUT/OUTPUT (I/O), but a map/reduce job with 
  multiple steps has to write to a file system multiple times. This is very inefficient!
- Map Reduce has been replaced by other technologies

<< :ref:`lesson5_8` | :ref:`lesson5_10`  >>


