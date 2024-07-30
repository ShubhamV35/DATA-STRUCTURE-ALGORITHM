


# https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    res1 = 0
    res2 = 0
    for i in range(len(apples)):
        apples[i] = apples[i] + a
        if apples[i] >=s and apples[i] <= t:
            res1 = res1 + 1
            
    for j in range(len(oranges)):
        oranges[j] = oranges[j] + b
        
        if oranges[j] >= s and oranges[j] <= t:
            res2 = res2 + 1
    
    print(res1)
    print(res2)
        
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)









