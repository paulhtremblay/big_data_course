with open('data/hadoop_words.txt', 'r') as read_obj:
    line = 'init'
    #THIS IS A STATE AND WON'T WORK IN HADOOP!
    word_count = {}
    while line:
