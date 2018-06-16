..  _day3_4:

=================================
Day 3 (4): Code and Bash Example
=================================

Mapper
======

.. literalinclude:: ../python_code/mapper.py
   :language: python
   :linenos:

``cat ../data/hadoop_words.txt | python mapper.py``

.. literalinclude:: ../python_code/reducer.py
   :language: python
   :linenos:

``cat ../data/hadoop_words.txt | ./mapper.py | sort |./reducer.py``
