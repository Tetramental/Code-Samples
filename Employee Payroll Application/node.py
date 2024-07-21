# File Name: node.py
# Purpose: To create a nodes used for a linked list
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: March 8, 2019
# ============================================================================
#                                                                   IMPORTANT
# ============================================================================
# Attributed Code from: Adelaida Medlock's CS 172 Lecture 07 about Nodes and Linked Lists
# ============================================================================

class Node:
    '''This class defines the structure and methods of a Node class.
    Methods of getting and setting the current and next nodes of data are available.'''
    
    # initalization method
    def __init__ (self, data, nextNode = None):
        self.__data = data
        self.__nextNode = nextNode
    
    # returns the data of the node
    def getData(self):
        return self.__data
    
    # returns the reference to the next node
    def getNext(self):
        return self.__nextNode
    
    # sets the data of the node
    def setData(self, new):
        self.__data = new
    
    # sets the reference to the next node
    def setNext(self, new):
        self.__nextNode = new
    
    # overloaded string method
    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__nextNode) + "."

# main program
if __name__ == "__main__":
    help(__name__)