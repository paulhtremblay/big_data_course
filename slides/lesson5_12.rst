..  _lesson5_12:

========================================
A Short Intro to Functional Programming
========================================



Class Exercise:
===============

Given this list:
`[1, 'f', 2, 3, 'g']`

You have to sum up all the items in the list that are not letters. Here is one way to do it:

::

 the_sum = 0
 for item in [1, 'f', '2, '3', 'g']:
      if isintance(item, int):
           the_sum += item
 print(the_sum)

Make this a functional program with no state.

Questions
=========

How is my example like the map/reduce programs? (Hint: Could we put the two lists on different machines?)
  

<< :ref:`lesson5_11` | :ref:`lesson5_13`  >>


