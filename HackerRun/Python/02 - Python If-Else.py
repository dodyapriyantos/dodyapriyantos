#!/bin/python3

import math
import os
import random
import re
import sys

def main(n):
    if n%2 == 1: print ('Weird')
    else:
        if (n>20): print ('Not Weird')
        else:
            if n >= 2 and n <= 5:
                print ('Not Weird')
            else:
                print ('Weird')


if __name__ == '__main__':
    n = int(input().strip())
    main(n)