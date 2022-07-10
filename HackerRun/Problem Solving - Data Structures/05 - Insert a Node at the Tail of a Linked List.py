#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtTail(head, data):
    
    dataOnNewNode = SinglyLinkedListNode(data)
    if (head == None) : return (dataOnNewNode)
    
    NewLlist = SinglyLinkedList()
    NewLlist.head = head
    NewLlist_head = NewLlist.head
    
    print('meme2')
    while (True):
        if NewLlist_head.next == None: 
            print('meme3')
            NewLlist_head.next = dataOnNewNode
            break
        NewLlist_head = NewLlist_head.next

    return (NewLlist.head)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
