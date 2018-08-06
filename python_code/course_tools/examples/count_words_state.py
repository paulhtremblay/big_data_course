#THIS IS A STATE AND WON'T WORK IN HADOOP OR DISTRUBTED SYSTEMS!
word_count = {}
# ^^^^^^^^^^^^^^
with open('simple_work_count_words.txt', 'r') as read_obj:
    line = 'init'
    while line:
        line = read_obj.readline()
        word_list = line.split()
        for word in word_list:
            if word_count.get(word) == None:
                word_count[word] = 0
            word_count[word] += 1
for key in sorted(list(word_count.keys())):
    print('{word}:{num}'.format(word = key, num = word_count[key]))
