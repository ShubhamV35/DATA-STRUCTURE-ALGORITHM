
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys



def breakingRecords(a):
    mini = a[0]
    maxi = a[0]

    res1 = 0
    res2 = 0

    for i in range(len(a)):
        if mini > a[i]:
            res2 = res2 + 1
            mini = a[i]
        if maxi  < a[i]:
            res1 = res1 + 1
            maxi = a[i]
    
    return [res1 , res2]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()











