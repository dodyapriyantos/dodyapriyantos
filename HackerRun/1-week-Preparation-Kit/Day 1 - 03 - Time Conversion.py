#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    #look if AM or PM
    if (s[-2:] == "AM"):
        #it is AM
        
        #remove the string of AM
        s = s[:-2]
        tempList = s.split(":")
        
        #ensure it is not 12AM
        if(s[:2] == "12"):
            tempList[0] = "00"
        return((tempList[0] + ":" + s[3:]))
        
    else:
        #it is PM
        
        #remove the string of PM
        s = s[:-2]
        
        if (s[:2] == "12"):
            return (s)
        else:
            #convert the hour time
            tempList = s.split(":")
            hourInt = int(tempList[0]) + 12
            return (str(hourInt) + ":" + s[3:])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
