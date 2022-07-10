#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    print('k = ' + str(k))
    print('len(A) = ' + str(len(A)))
    iteration = 0
    
    lenBefore = len(A)
    
    # specific use case
    if (A[0] == A[1]) and not(A[0]+1 in A) :
        print (len(A) - 2)
        return (len(A) - 2)
    
    for counter in range (0, len(A)):
        A.sort()
        if A[0] < k:
            if (len(A) == 1): return (-1)
            
            A[0] = A[0] + (2 * A.pop(1))
            iteration+=1; print(iteration)
            
            for counter in range (1,11):
                try:
                    if (A[counter] < k) and (A[counter+2] < k):
                        A[counter] = A[counter] + (2 * A.pop(counter+1))
                        iteration+=1; print(iteration)
                except:
                    A[0] = A[0]

        else:
            return (lenBefore - len(A))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
