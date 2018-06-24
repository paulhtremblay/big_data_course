..  _lesson4_4:

=============
Lesson 4 (4)
=============

Using Map Reduce to find the average tempeartures for each state
================================================================

The reducer
+++++++++++

Steps to create a reducer:


1. Read each line from the file. Set 3 values: current_state, current_state_count, and current_state_temp.
2. If the previous US state is the same, increase the counter by 1, and add to
   the current_state_temp
3. If the state is diffeent, calculate the average by dividing the
   current_state_temp/current_state_count
4. Print the result

.. literalinclude:: ../python_code/map_reduce/reduce_state_temps.py
   :language: python
   :linenos:

Questions
=========

1. What is the difference between this example and the word count example?
2. What are the similarities?
3. Would this example scale well (would it run fast for a really big data set)?
