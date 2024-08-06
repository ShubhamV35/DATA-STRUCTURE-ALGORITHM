




# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true



import math
import os
import random
import re
import sys


def birthday(s, d, m):

    counter = 0

    for i in range(len(s)):
        sum = 0
        if i+m <= len(s):
            for j in range(i,i+m):
                sum = sum + s[j]
            if sum == d:
                counter = counter + 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()




