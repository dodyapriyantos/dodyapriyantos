# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
import sys

StackStack = []

def main():
    global StackStack
    
    for line in sys.stdin:
        line = line.replace('\n', '')
        
        dataIN = (line.split(' '))
        if (dataIN[0] == '1'):
            #enqueue element from back
            StackStack.append(dataIN[1])
        elif (dataIN[0] == '2'):
            #dequeue front element
            del(StackStack[0])
        elif (dataIN[0] == '3'):
            #print front element
            print (StackStack[0])
        else:
            #first line is the total command. ignore it.
            temp = line
    
if __name__ == '__main__':
    main()
