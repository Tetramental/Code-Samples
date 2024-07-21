from node import Node
from employee import Employee

# File Name: linkedlist.py
# Purpose: To create a payroll linked list used for a payroll application
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: March 8, 2019
# ============================================================================
#                                                                   IMPORTANT
# ============================================================================
# Attributed Code from: Adelaida Medlock's CS 172 Lecture 07 about Nodes and Linked Lists
# ============================================================================

class LinkedList:
    '''This class defines the structure and methods of a LinkedList class.
    The following methods with their return values are available:
    1) isEmpty [boolean]
    2) search [boolean]
    3) append [None]
    4) remove [None]
    5) __getitem__ [varies]
    6) __str__ [string]
    7) __len__ [integer]'''
    
    # initialization method
    def __init__(self):
        self.__head = None
    
    # determines if the linked list is empty
    def isEmpty(self):
        return self.__head == None
    
    # searches if a node exists in the linked list; also returns the index it was found in
    def search(self, item):
        current = self.__head
        index = 0
        found = False
        while current != None and not found:
            if current.getData().getEmployeeID() == item.getEmployeeID():
                found = True
            else:
                current = current.getNext()
                index += 1
        return index, found
    
    # appends a new node to the end of the linked list
    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
    
    # removes an existing node from any part of the linked list
    def remove(self, existingNode):
        current = self.__head
        previous = None
        found = False
        
        # find item in list
        while not found:
            if current.getData() == existingNode:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        # item was in the first node, otherwise item was somewhere after the first node
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    # overloaded index method
    def __getitem__(self, index):
        current = self.__head
        for i in range(index):
            current = current.getNext()
        if current == None:
            return None
        return current.getData()
    
    # overloaded string method
    def __str__(self):
        result = ""
        current = self.__head
        while current != None:
            result += str(current.getData()) + " --> "
            current = current.getNext()
        return result
    
    # overloaded length method
    def __len__(self):
        if self.__head == None:
            return 0
        current = self.__head
        counter = 1
        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter

# main program
if __name__ == "__main__":
    help(__name__)