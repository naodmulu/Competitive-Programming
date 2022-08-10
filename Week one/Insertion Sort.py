#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
        
    stored_value = arr[-1]
    m = n - 1
    while m  > 0 and stored_value < arr[m-1]:
        arr[m] = arr [m-1]
        m-=1
        print(*arr)
    arr[m] = stored_value
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
