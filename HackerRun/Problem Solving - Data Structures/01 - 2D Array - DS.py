#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    
    # brute force calculation # 1 attempt
    #return(calculate_hourglass_16_1attempt(arr))
    
    #using for loops # 2 attempt
    #return(calculate_hourglass_16_2attempt(arr))
    
    #using for loops # 3 attempt
    #return(calculate_hourglass_16_3attempt(arr))
    
    #using for loops and max API from math # 4 attempt
    return(calculate_hourglass_16_4attempt(arr))

#4th attempt
def calculate_hourglass_16_4attempt(arr):
    #temp = []
    max_value=-999999999999
    for j in range (int(len(arr)/2)+1):
        for i in range (int(len(arr)/2)+1):
            max_value = max(max_value,(arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2] + arr[j+1][i+1]))

    #return the biggest value
    return (max_value)
    
#3rd attempt
def calculate_hourglass_16_3attempt(arr):
    temp = []
    for j in range (int(len(arr)/2)+1):
        for i in range (int(len(arr)/2)+1):
            temp.append(arr[j][i] + arr[j][i+1] + arr[j][i+2] + arr[j+2][i] + arr[j+2][i+1] + arr[j+2][i+2] + arr[j+1][i+1])
    #sort it descending
    temp.sort(reverse=True)
    #return the biggest value
    return (temp[0])
    
#2nd attempt
def calculate_hourglass_16_2attempt(arr):
    temp = []
    #1st line
    for i in range (int(len(arr)/2)+1):
        temp.append(arr[0][i] + arr[0][i+1] + arr[0][i+2] + arr[2][i] + arr[2][i+1] + arr[2][i+2] + arr[1][i+1])
    #2nd line
    for i in range (int(len(arr)/2)+1):
        temp.append(arr[1][i] + arr[1][i+1] + arr[1][i+2] + arr[3][i] + arr[3][i+1] + arr[3][i+2] + arr[2][i+1])
    #3rd line
    for i in range (int(len(arr)/2)+1):
        temp.append(arr[2][i] + arr[2][i+1] + arr[2][i+2] + arr[4][i] + arr[4][i+1] + arr[4][i+2] + arr[3][i+1])
    #4th line
    for i in range (int(len(arr)/2)+1):
        temp.append(arr[3][i] + arr[3][i+1] + arr[3][i+2] + arr[5][i] + arr[5][i+1] + arr[5][i+2] + arr[4][i+1])
    #sort it ascending
    temp.sort()
    #return the biggest value
    return (temp[-1])
    
#1st attempt
def calculate_hourglass_16_1attempt(arr):
    temp = []
    #1st line
    one_one   = arr[0][0] + arr[0][1] + arr[0][2] + arr[2][0] + arr[2][1] + arr[2][2] + arr[1][1]
    one_two   = arr[0][1] + arr[0][2] + arr[0][3] + arr[2][1] + arr[2][2] + arr[2][3] + arr[1][2]
    one_three = arr[0][2] + arr[0][3] + arr[0][4] + arr[2][2] + arr[2][3] + arr[2][4] + arr[1][3]
    one_four  = arr[0][3] + arr[0][4] + arr[0][5] + arr[2][3] + arr[2][4] + arr[2][5] + arr[1][4]
    temp.append(one_one);temp.append(one_two);temp.append(one_three);temp.append(one_four);
    #2nd line
    two_one   = arr[1][0] + arr[1][1] + arr[1][2] + arr[3][0] + arr[3][1] + arr[3][2] + arr[2][1]
    two_two   = arr[1][1] + arr[1][2] + arr[1][3] + arr[3][1] + arr[3][2] + arr[3][3] + arr[2][2]
    two_three = arr[1][2] + arr[1][3] + arr[1][4] + arr[3][2] + arr[3][3] + arr[3][4] + arr[2][3]
    two_four  = arr[1][3] + arr[1][4] + arr[1][5] + arr[3][3] + arr[3][4] + arr[3][5] + arr[2][4]
    temp.append(two_one);temp.append(two_two);temp.append(two_three);temp.append(two_four);
    #3rd line
    three_one   = arr[2][0] + arr[2][1] + arr[2][2] + arr[4][0] + arr[4][1] + arr[4][2] + arr[3][1]
    three_two   = arr[2][1] + arr[2][2] + arr[2][3] + arr[4][1] + arr[4][2] + arr[4][3] + arr[3][2]
    three_three = arr[2][2] + arr[2][3] + arr[2][4] + arr[4][2] + arr[4][3] + arr[4][4] + arr[3][3]
    three_four  = arr[2][3] + arr[2][4] + arr[2][5] + arr[4][3] + arr[4][4] + arr[4][5] + arr[3][4]
    temp.append(three_one);temp.append(three_two);temp.append(three_three);temp.append(three_four);
    #4th line
    four_one   = arr[3][0] + arr[3][1] + arr[3][2] + arr[5][0] + arr[5][1] + arr[5][2] + arr[4][1]
    four_two   = arr[3][1] + arr[3][2] + arr[3][3] + arr[5][1] + arr[5][2] + arr[5][3] + arr[4][2]
    four_three = arr[3][2] + arr[3][3] + arr[3][4] + arr[5][2] + arr[5][3] + arr[5][4] + arr[4][3]
    four_four  = arr[3][3] + arr[3][4] + arr[3][5] + arr[5][3] + arr[5][4] + arr[5][5] + arr[4][4]
    temp.append(four_one);temp.append(four_two);temp.append(four_three);temp.append(four_four);
    #sort it ascending
    temp.sort()
    #return the biggest value
    return (temp[-1])
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
