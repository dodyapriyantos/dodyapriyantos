#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    #iniialization
    positiveData = 0
    negativeData = 0
    zeroData = 0
    
    #how many data in the list
    manyData = len(arr)
    
    for inputArr in arr:
        if (inputArr > 0):
            positiveData+=1
        elif (inputArr < 0):
            negativeData+=1
        else:
            zeroData+=1 
    
    print("{:.6f}".format(positiveData/manyData))
    print("{:.6f}".format(negativeData/manyData))
    print("{:.6f}".format(zeroData/manyData))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
