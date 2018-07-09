..  _lesson2_16:


===========
Run X2GO
===========

3. Launch x2go and fill in the right fields

.. image:: img/x2go_siginin.png

And..

.. image:: img/x2go_logging_in.png

Install Needed Software
========================

::

 conda create -n class
 source activate class
 conda install bokeh pyshp Shapely jupyter
 wget https://s3-us-west-2.amazonaws.com/paulhtremblaypublic/python_code/python_big_data_tools-.21.tar.gz
 tar -xvzf python_big_data_tools-.2.tar.gz
 cd python_big_data_tools-.2/
 python setup.py install

<< :ref:`lesson2_15` | :ref:`lesson3`  >>

