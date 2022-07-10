#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    # firstly, we sort the data in the list
    arr.sort()
    
    resultMin = 0
    resultMax = 0 
    
    counter = 0
    for datadata in arr:
        if (counter <= 3):
            resultMin += arr[counter]
        counter+=1
    
    counter = 0
    for datadata in arr:
        if (counter <= 3):
            resultMax += arr[counter+1]
        counter+=1
    
    print(str(resultMin) + " " + str(resultMax))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
