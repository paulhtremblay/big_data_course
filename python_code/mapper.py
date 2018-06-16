#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.strip().split()
    # increase counters
    for word in words:
        print('{word}\t{num}'.format(word = word, num = 1))
