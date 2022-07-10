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
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):

    # init the Final ListNode
    MergeTheSameDataValue = SinglyLinkedListNode(None)
    
    # use a temporary Node as merger Node to work on
    temp_node = MergeTheSameDataValue

    # work on the merging. except the last one.
    while (head1 and head2):
        if (head1 == None) and (head2 != None):
            temp_node.next = head2
            head2 = head2.next
        elif(head2 == None) and (head1 != None):
            temp_node.next = head1
            head1 = head1.next
        elif (head1.data <= head2.data):
            temp_node.next = head1
            head1 = head1.next
        else:
            temp_node.next = head2
            head2 = head2.next
        temp_node = temp_node.next
        
    # last component to merge
    if head1: temp_node.next = head1
    if head2: temp_node.next = head2
    
    return(MergeTheSameDataValue.next)



if __name__ == '__main__':