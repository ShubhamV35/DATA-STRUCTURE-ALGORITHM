

# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys



def timeConversion(s):

    form = s[len(s)-2] + s[len(s)-1]
    hour = s[0] + s[1]
    minute = s[3] + s[4]
    second = s[6] + s[7]


    if form =='PM' and hour == '12':
        s = hour+':'+minute+':'+second
        return s

    if form == 'PM' and hour != '12':
        hour = int(hour) + 12
        s = str(hour)+':'+minute+':'+second
        return s

    if form == 'AM' and hour  == '12':
        s = '00'+':'+minute+':'+second
        return s

    else:
        # hour = int(hour) + 12
        s = str(hour)+':'+minute+':'+second
        return s



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

