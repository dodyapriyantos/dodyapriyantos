# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import os

stacked = [""]
text_stack = ''

# counter for first line. no need to do anything
counter_FirstLine = 1

# read each line stdin
for line in sys.stdin:
    #start from 2nd lines
    if counter_FirstLine > 1:
        
        # remove "endline or \n"
        if line[-1] == '\n':
            line = line[:-1]
        
        #start text editor
        if (line[0] == '1'):
            #append the current data, and save it to stack
            stacked.append(stacked[-1] + (line[2:]))
            
        elif((line[0] == '2')):
            #delete a few string from current latest stack, and save it to stack
            stacked.append((stacked[-1])[:int(-1 * (int(line[2:])))])
            
        elif(line[0] == '3'):
            #print from the latest stack. a specific index only
            print ((stacked[-1])[(int(line[2:])-1)] )
            
        elif (line[0] == '4'):
            #Undo, by simply pop it
            stacked.pop()
            
    #just a counter
    counter_FirstLine=2
