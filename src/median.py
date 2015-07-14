# Author: Gabriel A. von Winckler <winckler@campogeral.com.br>
# This code is part of an execise. After evaluation, will be released as
# GPL version 3.

class MedianByFrequency(object):
    """Calculate median by keeping the frequency of elements from a
         fixed range.

    This method uses a table of frequencies to avoid keep all elements.
    Doing so, it can keep the memory usage constant, as well time to
      update the set and compute the median.

    This routine also optimize the lookup of median in the table of
    frequencies. It's optional (without the routine is already O(const)),
    but it reduce the number of operations using a slightly complex
    bookkeeping."""

    def __init__(self, max_element):
        # max_element is the max value to be accepted.
        #  it defines the range of values
        self.freq = [0] * max_element # table of frequencies
        self.count = 0 # number of elements
        self.n = 0 # current median value
        self.n_count = 0 # index of the current median value in use.

    # Is the number of elements even?
    def _even(self):
        return not bool(self.count % 2)

    # what would be the next (bigger) value
    def _next(self):
        if (self.n_count + 1) < self.freq[self.n]:
            return self.n
        else:
            # exhausted n
            next_n = self.n
            while (next_n < (len(self.freq) - 1)):
                next_n += 1
                if self.freq[next_n] > 0:
                    return next_n
        # No other element found ("adding first element, been 0" case)
        return 0

    # what would be the previous (smaller) value
    def _prev(self):
        if self.n_count > 0:
            return self.n
        else:
            # exhausted n
            prev_n = self.n
            while (prev_n >= 0):
                prev_n -= 1
                if self.freq[prev_n] > 0:
                    return prev_n
        # No other element found
        return 0

    # add new value to the set
    def update(self, value):
        self.freq[value] += 1
        self.count += 1

        # bookkeeping to avoid transverse the array every time
        if value >= self.n and self._even():
            pass
        if value < self.n and not self._even():
            pass

        if value >= self.n and not self._even():
            # move right
            if self._next() == self.n:
                self.n_count += 1
            else:
                self.n = self._next()
                self.n_count = 0

        if value < self.n and self._even():
            # move left
            if self._prev() == self.n:
                self.n_count -= 1
            else:
                self.n = self._prev()
                self.n_count = self.freq[self.n] - 1

    # get current median
    def get(self):
        if self._even():
            return (self.n + self._next()) / 2.0
        else:
            return self.n
