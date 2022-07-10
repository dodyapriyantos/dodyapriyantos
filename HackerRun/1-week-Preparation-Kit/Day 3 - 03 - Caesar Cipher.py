#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    
    tempProcessString = s
    tempRotation = k
    
    tempListFinal = []
    for counterLetter in range (0, len(tempProcessString)):
        ValueToCheck = int(ord(tempProcessString[counterLetter]))
        if  (ValueToCheck < 65):
            tempListFinal.append(tempProcessString[counterLetter])
        elif (((ValueToCheck > 90) and (ValueToCheck < 97))): 
            tempListFinal.append(tempProcessString[counterLetter])
        elif (ValueToCheck > 122):
            tempListFinal.append(tempProcessString[counterLetter])
        else:
            temptemp = (tempProcessString[counterLetter])
            for iteratioii in range (0, tempRotation):
                if (temptemp == 'z'):
                    temptemp = 'a'
                elif(temptemp == 'Z'):
                    temptemp = 'A'
                else:
                    temptemp = chr(int(ord(temptemp)) + int(1))
            tempListFinal.append(temptemp)
        counterLetter+=1    
    return (''.join(tempListFinal))
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
