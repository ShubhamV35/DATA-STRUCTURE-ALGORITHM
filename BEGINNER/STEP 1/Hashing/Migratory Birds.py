
# https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true




import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(a):

    hashmap = [0]*6

    for i in a:
        hashmap[i] = hashmap[i] + 1

    maxi = max(hashmap)
    for i in range(len(hashmap)):
        if hashmap[i] == maxi:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
