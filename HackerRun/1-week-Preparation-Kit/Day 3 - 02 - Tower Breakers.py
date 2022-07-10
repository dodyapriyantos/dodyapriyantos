#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    
    # before start, double check all tower is more than 1 height. 
    # if all tower have heigth of 1, then winner is player 2
    if (m <= 1):
        return (2)
    
    if (n%2 == 1) and (m%2 == 1):
        return(1)
    elif (n%2 == 0) and (m%2 == 1):
        return(2)
    elif (n%2 == 0) and (m%2 == 0):
        return(2)
    else:
        return(1)
        
    # 1st reduce
    towerreduce = m / 2
    m -= towerreduce
    if (m == 1):
        if(n % 2 == 0):
            return(1)
        else:
            return(2)
    
    manytower = [m] * n
    
    PlayerWin = 0
    winner = False
    while (winner == False):

        #player move
        #print ("player 1 move") 
        if (winner == False):
            iTower = choosetower(manytower)
            ToTake = HowManyToTake(manytower[iTower])
            if (ToTake == 0):
                PlayerWin = 2
                winner = True
            else:
                manytower[iTower] -= ToTake
        
        #player 2 move
        if (winner == False):
            iTower = choosetower(manytower)
            ToTake = HowManyToTake(manytower[iTower])
            if (ToTake == 0):
                PlayerWin = 1
                winner = True
            else:
                manytower[iTower] -= ToTake
            
    return (PlayerWin)

def choosetower(TowerToChoose):
    tempChoose = TowerToChoose
    tempChoose.sort()
    return (TowerToChoose.index(tempChoose[-1]))

def HowManyToTake(totake):
    for ii in range (totake, 0, -1):
        if (totake % ii == 0):
            return (ii)
    return(0)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
