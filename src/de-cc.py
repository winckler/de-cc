#!/usr/bin/env python
# Author: Gabriel A. von Winckler <winckler@campogeral.com.br>
# This code is part of an execise. After evaluation, will be released as
# GPL version 3.

import os

# Custom median class to avoid keep all elements
from median import MedianByFrequency

# Sanity check on input file
input_file = os.path.join('tweet_input', 'tweets.txt')
try:
    input1 = open(os.path.join('tweet_input', 'tweets.txt'))
except IOError:
    print("Error: can't open input file.")
    exit(1)

# Sanity check on output files
if not os.path.isdir('tweet_output'):
    try:
        os.mkdir('tweet_output')
    except OSError:
        print("Error: can't create (missing) output directory.")
        exit(1)
try:
    output1 = open(os.path.join('tweet_output', 'ft1.txt'), 'w')
    output2 = open(os.path.join('tweet_output', 'ft2.txt'), 'w')
except IOError:
    print("Error: can't open output file.")
    exit(1)

# Let's work
word_count = {} # dict with all found words and it's count
freq = MedianByFrequency(160) # custom median object

for tweet in input1:
    # new set to count uniq words in each tweet
    uniq_words = set()

    # trim the last '\n' and split by spaces
    for word in tweet.strip().split(' '):
        # skip "empty" words (set of spaces)
        if word:
            # increase word count
            word_count[word] = word_count.get(word, 0) + 1
            # add to the local set
            uniq_words.add(word)

    # update median and print (fn2.txt)
    freq.update(len(uniq_words))
    output2.write("%.1f\n" % freq.get())

# sort and print (fn1.txt)
for word in sorted(word_count.keys()):
    output1.write("%s %d\n" % (word.ljust(27), word_count[word]))

output1.close()
output2.close()
