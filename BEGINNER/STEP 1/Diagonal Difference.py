
# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(a):
    left = 0
    right = 0
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                left = left + a[i][j]
                
                right = right + a[i][len(a)-1-i]
    return abs(left - right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()








