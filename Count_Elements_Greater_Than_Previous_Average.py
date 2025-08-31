#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    
    if len(responseTimes) < 2:
        return 0
    count = 0
    previousSum = responseTimes[0]
    
    for i in range(1, len(responseTimes)):
        a = responseTimes[i]
        avg = previousSum/i
        previousSum+=a
        if a > avg:
            count+=1
    return count
              
        
if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
