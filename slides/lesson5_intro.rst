..  _lesson5_intro:

=========================================
Lesson 5 Map Reduce with Multiple Steps
=========================================

Do Hotter Climates have more or less rainfall?
===============================================

In order to answer the above question, we need to create two map and reduce jobs. Here are the steps:

1. Create a mapper for each weather station
2. Create a reducer that calculates the average
3. Form a dictionary, with the keys being a temperature range, and the values the station ids.
4. Use the dictionary from step (3) to create a second mapper, with the key being the temperature range, 
   and the values the rainfall
5. Create a reducer to average the rainfall
