#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

row = 0
colomn = 0

def gridChallenge(grid):
    global row
    global colomn
    
    # Write your code here
    saveAcopy = grid
    
    if (len(grid) == 1):
        return("YES")
    
    row = len(grid[0])
    colomn = len(grid)
    
    tempProcess11 = []
    for x in range (0, colomn):
        temprocess22 = []
        for y in range (0, row):
            temprocess22.append(int(ord(grid[x][y])))
        tempProcess11.append(temprocess22)
    
    for x in range (0, colomn):
        tempProcess11[x].sort()

    #check column only. Row always going to be able to be sorted.
    if (checkColoumn(tempProcess11) == True):
        return("YES")
    else:
        return("NO")
    
def checkColoumn(GridtoCheck):
    global row
    global colomn
    for x in range (0, row):
        for y in range (0, colomn-1):
            if (GridtoCheck[y][x] > GridtoCheck[y+1][x]):
                return (False) 
    return(True)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
