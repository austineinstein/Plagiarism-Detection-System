#!/usr/bin/env python
import sys
cur_word = None
cur_count = 0
word = None
SP = 0
EP = 0
for line in sys.stdin:
    line = line.strip()
    word, count, SP, EP = line.split('_', 3)
    try:
       count = int(count)
    except ValueError:
       # something went bad - oh well
       continue
    # key-sorted already
    if cur_word == word:
       cur_count += count
    else:
       if cur_word:
            print '%s%s_%s%s' % (cur_word, cur_count, SP, EP) 
       cur_count = count
       cur_word = word
# don't forget the last word
if cur_word == word:
    print '%s%s_%s%s' % (cur_word, cur_count, SP, EP)
    #output values to text file