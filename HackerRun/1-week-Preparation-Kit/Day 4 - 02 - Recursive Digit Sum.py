#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    
    #ToProcess = ""
    #for i in range (0, k):
    #    ToProcess += n
    #
    #valueFinal = int(ToProcess)
    #while (valueFinal >= 10):
    #    ToProcess = str(valueFinal)
    #    superdigitYY = 0
    #    for i in range (0, len(ToProcess)):
    #        superdigitYY += int(ToProcess[i])
    #    valueFinal = superdigitYY
    #return(valueFinal)
    
    ToProcess = n
    multiplier = k
    valueFinal = int(ToProcess)
    
    # 1st time SuperDigit
    valueFinal = superdigitMini(valueFinal)
        
    # multiply the k
    valueWithMultiplier = valueFinal * k
    
    # redo super digit
    while (valueWithMultiplier >= 10):
        valueWithMultiplier = superdigitMini(valueWithMultiplier)
        
    return(valueWithMultiplier)
    
def superdigitMini(valueFinal):
    while (valueFinal >= 10):
        ToProcess = str(valueFinal)
        superdigitYY = 0
        for i in range (0, len(ToProcess)):
            superdigitYY += int(ToProcess[i])
            print (superdigitYY)
        valueFinal = superdigitYY
    return (valueFinal)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
