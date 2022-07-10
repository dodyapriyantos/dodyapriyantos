#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def legoBlocks(n, m):
    # Write your code here

    #height = n
    #width = m
    #block_1 = [1         ]
    #block_2 = [1, 1      ]
    #block_3 = [1, 1, 1   ]
    #block_4 = [1, 1, 1, 1]
    #
    #blocks = [[], block_1, block_2, block_3, block_4]
    #
    #AllPossibilities = False
    #possible_permutation = []
    #counter = 0
    #possible = True
    #Permutation = 0
    #
    #block_m_4 = \
    #[
    #[blocks[4]], \
    #[blocks[3], blocks[1]], \
    #[blocks[1], blocks[3]], \
    #[blocks[2], blocks[2]], \
    #[blocks[1], blocks[1] , blocks[2]], \
    #[blocks[2], blocks[1] , blocks[1]], \
    #[blocks[1], blocks[2] , blocks[1]], \
    #[blocks[1], blocks[1] , blocks[1] , blocks[1]]
    #]
    #
    ##block_m_4 = []
    ###4.1  [1, 1, 1, 1]
    ##block_m_4.append([blocks[4]])
    ###4.2  [[1, 1, 1], [1]]
    ##block_m_4.append([blocks[3], blocks[1]])
    ###4.3  [[1], [1,1,1]]
    ##block_m_4.append([blocks[1], blocks[3]])
    ###4.4  [[1, 1], [1,1]]
    ##block_m_4.append([blocks[2], blocks[2]])
    ###4.5  [[1], [1], [1,1])
    ##block_m_4.append([blocks[1], blocks[1] , blocks[2]])
    ###4.6  [[1, 1], [1], [1]]
    ##block_m_4.append([blocks[2], blocks[1], blocks[1]])
    ###4.7  [[1], [1,1], [1]]
    ##block_m_4.append([blocks[1], blocks[2], blocks[1]])
    ###4.8  [[1], [1], [1], [1]]  
    ##block_m_4.append([blocks[1],blocks[1],blocks[1],blocks[1]])
    #
    #block_m_3 = []
    ##3.1  [1, 1, 1]
    #block_m_3.append([blocks[3]])
    ##3.2  [[1], [1,1]]
    #block_m_3.append([blocks[1], blocks[2]])
    ##3.3  [[1,1], [1]]
    #block_m_3.append([blocks[2], blocks[1]])
    ##3.4  [[1, 1], [1,1]]
    #block_m_3.append([blocks[2],blocks[2]])
    #
    #block_m_2 = []
    ##2.1  [[1],[1]]
    #block_m_2.append([blocks[1],blocks[1]])
    ##2.2  [[1,1]]
    #block_m_2.append([blocks[2]])
    #
    #block_m_1 = []
    ##1.1  [[1]]
    #block_m_1.append([blocks[1]])
    #
    #print ('dody 11')
    #print (block_m_4)
    #print (block_m_3)
    #print (block_m_2)
    #print (block_m_1)
    #
    ##level number : 
    #for counter_height in range(1, n+1):
    #    print('dody 22')
    #    possibility = False
    #    
    #    left = m
    #    # width number :
    #    for counter_width in range (1, m+1):
    #        if left >= 4 :
    #            print('dody 04')
    #            possible_permutation.append(block_m_4) #8
    #            left = left-4
    #        elif left == 3:
    #            print('dody 03')
    #            possible_permutation.append(block_m_3) #4
    #            left = left-3
    #        elif left == 2:
    #            print('dody 02')
    #            possible_permutation.append(block_m_2) #2
    #            left = left-2
    #        elif left == 1:
    #            print('dody 01')
    #            possible_permutation.append(block_m_1) #1
    #            left = left-1
    #        else:
    #            print('dody 00')
    #            left = left  
    #            
    #    print (possible_permutation)
    #    print (len(possible_permutation[0]))
    #    print (len(possible_permutation[1]))
    #               
    #            #1.1  [blocks[1] * 4])
    #            
    #            #2.1  possible.append([blocks[1] * 2])
    #            #2.2  possible.append([blocks[2] * 1])
    #            
    #            #3.1  possible.append([blocks[1] * 3])
    #            #3.2  possible.append([blocks[1] * 2, blocks[2] * 1])
    #            #3.3  possible.append([blocks[1] * 1, blocks[2] * 1], blocks[1] * 1)
    #            #3.4  possible.append([blocks[2] * 1, blocks[1] * 2])
    #                
    #            #4.1  possible.append([blocks[4] * 1])
    #            #4.2  possible.append([blocks[3] * 1], [blocks[1] * 1])
    #            #4.3  possible.append([blocks[1] * 1], [blocks[3] * 1])
    #            #4.4  possible.append([blocks[2] * 1], [blocks[2] * 1])
    #            #4.5  possible.append([blocks[2] * 1], [blocks[1] * 2])
    #            #4.6  possible.append([blocks[1] * 1], [blocks[2] * 1], [blocks[1] * 1])
    #            #4.7  possible.append([blocks[1] * 2], [blocks[2] * 1])
    #            #4.8  possible.append([blocks[1] * 4])             
          
    
    #4.1  [1, 1, 1, 1]
    #4.2  [[1, 1, 1], [1]]
    #4.3  [[1], [1,1,1]]
    #4.4  [[1, 1], [1,1]]
    #4.5  [[1], [1], [1,1])
    #4.6  [[1, 1], [1], [1]]
    #4.7  [[1], [1,1], [1]]
    #4.8  [[1], [1], [1], [1]]  
    #
    #3.1  [1, 1, 1]
    #3.2  [[1], [1,1]]
    #3.3  [[1,1], [1]]
    #3.4  [[1, 1], [1,1]]
    #
    #2.1  [[1],[1]]
    #2.2  [[1,1]]
    #
    #1.1  [[1]]
    
    
    height = n
    width = m
    
    #available Good + Bad on 1 width
    P = [0, 1, 2, 4, 8]
    for i in range(5,1001):
        P.append(P[i-1] + P[i-2] + P[i-3] + P[i-4])
    #print(P)
    
    # Possible (Good-Bad) on m and n
    possibility_good = pow(P[width], height)
    
    # Possible Bad
    Final_Good = ( possibility_good - (1 + pow(width,(width - 1)) - width) )
    
    #print(str(Permutation))
    return(Final_Good)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
