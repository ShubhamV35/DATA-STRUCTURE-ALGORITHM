
# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true


import math
import os
import random
import re
import sys


def bonAppetit(a, k, b):

    total = (sum(a) - a[k])/2

    if total != b:
        print(int(b - total))

    else:
        print('Bon Appetit')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
