#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here

    counterBribe = 0;
    # reduce the value inside q List with 1
    i=0
    for datadata in q: q[i]=datadata-1;i+=1
    # enumerate the list for easier counter
    for i,datadata in enumerate(q):
        # check if each component had got bribe many times
        if ((datadata-i) > 2): print ("Too chaotic"); return;
        # check for each component if they had received bribe
        for j in range (0 if ((datadata-1)<0) else (datadata-1),i) :
            if (datadata < q[j]): counterBribe += 1;
    #print final Counter Bribe happened
    print(counterBribe);
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
