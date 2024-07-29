
# https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true


import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
            
        for k in range(i+1):
            print("#",end="")
        print()
            
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
