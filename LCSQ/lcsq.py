import time
# This program has a time complexity of O((k))
# where k = length of strings
import sys
from itertools import product
from collections import defaultdict


if __name__ == '__main__':
    s1 = raw_input('Enter String 1\n')
    s2 = raw_input('Enter String 2\n')
    #print s1,s2
    run_time=time.time()

    dp = defaultdict(str)
    for x, y in product(range(len(s1)), range(len(s2))):
        if s1[x] == s2[y]:
            dp[(x, y)] = dp[(x-1, y-1)] + s1[x]
        else:
            dp[(x, y)] = max(dp[(x-1, y)], dp[(x, y-1)], key=len)
    print(dp[len(s1)-1, len(s2)-1])

    print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"

