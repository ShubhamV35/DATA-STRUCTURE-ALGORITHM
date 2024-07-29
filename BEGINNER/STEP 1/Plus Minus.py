


#  https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

# Code

#!/bin/python3

import math
import os
import random
import re
import sys



def plusMinus(arr):
    
    pos = 0
    neg = 0
    zero = 0
    
    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        else:
            zero = zero + 1
            
    pos = pos/len(arr)
    neg = neg/len(arr)
    zero = zero/len(arr)
    
    pos = f"{pos:.6f}"
    neg = f"{neg:.6f}"
    zero = f"{zero:.6f}"
    print(pos)
    print(neg)
    print(zero)


    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
