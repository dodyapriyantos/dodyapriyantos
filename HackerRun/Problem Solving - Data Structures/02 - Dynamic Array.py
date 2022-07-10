#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

#create global variable
arr = []
lastAnswer = 0
AnswerList = []

def dynamicArray(n, queries):
    # Write your code here
    global arr, AnswerList
    
    #create arr list with empty inside
    for i in range (n): arr.append([])
    
    #dispatch the command: 1 and 2 (or else)
    for listlist in queries:
        if listlist[0] == 1:
            queries_one(n, listlist)
        else:
            queries_two(n, listlist)
    
    #return the answer as list
    return(AnswerList)

#queries with command 1
def queries_one(n, command):
    global lastAnswer, arr
    idx = (command[1] ^ lastAnswer) % n
    (arr[idx]).append(command[2])
    
#queries with command 2
def queries_two(n, command):
    global lastAnswer, arr, AnswerList
    idx = (command[1] ^ lastAnswer) % n
    idy = (command[2] % len(arr[idx]))
    lastAnswer = arr[idx][idy]
    AnswerList.append(lastAnswer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
