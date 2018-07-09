..  _lesson6_5:

=======================================
Anatomy Behind A Spark Job
=======================================

Transformations
===============

Narrow Transformations
------------------------

All elements needed are on the *same* partition

- map
- flatMap
- mapPartition
- filter
- sample
- union

Wide Transformations
---------------------

Elements needed are on *different* partitions

- intersection
- distinct
- reduceByKey
- groupByKey
- join
- cartesian
- repartition
- coalesce

Actions
=======

- collect
- count
- countByValue
- reduce
- fold
- take


<< :ref:`lesson6_4` | :ref:`lesson6_6`  >>

