#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    total_swaps = 0
    for i in range(len(a)-1):
        swaps = 0
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
               a[j],a[j+1]=a[j+1],a[j]
               swaps += 1
               total_swaps += 1
        if swaps == 0:
            break
    print("Array is sorted in {} swaps.".format(total_swaps))
    print ("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
