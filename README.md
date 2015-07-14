# Introduction

This is a solution to a Data Engineering toy problem.

(The reference to the original problem is intentionally missing until the submission deadline is over)

# Rationally

The first feature could be implemented in a distributed way. It easily fits the map/reduce model. But the second feature has a hard dependency requiring all lines to be processed in order, sequentially. Due to that and the statement in FAQ saying the code will be evaluated in a single machine, a parallel or distributed solution was avoided for simplicity.

The focus was create a implementation that scales well (perferable linear) with the number of input lines.

The first feature uses a dictionary data structure in python, with constant access time and scaling in-memory with the number of unique words, not input lines. The final print step requires sorting, done only once, and scaling with the number of unique words. The default python implementation of sort was used, and most likely will scale with O(n log n), n being the number of words.

The second feature uses a custom class to calculate and update the median, keeping the previous information on a frequency table instead of keeping the values itself. This allows a constant memory footprint and computational time. A optimization has employed to reduce the number of operations on the frequency table. Without it, the time is still constant, but requires a greater set of operations. In other hand, this optimization required some extra bookkeeping, making the code a little less obvious.

# Dataset

It's hard to find a freely available twitter dataset. In the lack of one, some datasets were generated using the _fortune_ program (Unix rules!).

The bash code used was:

```
i=0
while [ $i -lt 1000000 ]
do
  fortune | tr '\n' ' ' | tr '\t' ' ' | sed -e 's/  */ /g' | cut -c 1-160
  i=$((i+1))
done > 1000000.txt
```

# Environment

The code was written in Python, only using standard modules, compatible with python versions 2 (2.7) and 3. The tests were evaluated in a GNU/Linux, Ubuntu 15.4, with python 2.7.9 and 3.4.3.

# Results

The code was benchmarked with 5 datasets: 1K, 10K, 100K, 1M, 10M elements.

samples | user time (s)
--------|--------------
1K      | 0.054
10K     | 0.170
100K    | 1.34
1M      | 13.4
10M     | 134

# Author

Gabriel A. von Winckler <winckler@campogeral.com.br>
