..  _lesson5_13:

========================================
A Short Intro to Lazy Programming
========================================

The following code ads up al the numbers from 1 to n.


.. literalinclude:: ../python_code/examples/sum_nums.py
   :language: python
   :linenos:

The function stores all the numbers in a list before summing them
up. What happens if the list was really large? We would use a lot of memory
when we don't have to. We only want the answer, so there is no need to 
create a list.

.. literalinclude:: ../python_code/examples/sum_nums_lazy.py
   :language: python
   :linenos:

Notes:

- the generator is *lazy*. It only evaluates the numbers when it has to.
the second function is a generator. You can also access it this way

::

 gen = first_n_as_lazy(3)
 print(next(gen))

- copy that code to Jupyter. Run `next(gen)` 3 more times. What hapens? 

You can also access a generator with this code:

::

 gen = first_n_as_lazy(3)
 for num in gen:
    print(num)

When you program, be lazy!

Questions
=========

1. What is the main advantage of lazy processing? 

Class Exercise
===============


<< :ref:`lesson5_12_2` | :ref:`lesson6`  >>


