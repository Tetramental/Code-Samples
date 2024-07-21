import pygame
import abc

# File Name: drawable.py
# Purpose: The Drawable class used for the simple game
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 22, 2019

class Drawable(metaclass = abc.ABCMeta):
    '''A class in which all classes that extend from this class are considered "Drawable".
    Consists of two abstract methods'''
    
    # initialization method
    def __init__(self, x = 0, y = 0, visible = True):
        self.__x = x
        self.__y = y
        self.__visible = visible

    # returns a tuple of the location of a Drawable object
    def getLocation(self):
        return (self.__x, self.__y)

    # returns the visibility of the object
    def getVisibility(self):
        return self.__visible

    # sets the location of the Drawable object through a tuple
    def setLocation(self, p):
        self.__x = p[0]
        self.__y = p[1]

    # sets the visibility of the Drawable object
    def setVisibility(self, visible):
        self.__visible = visible

    # draw method must be present in all classes that inherit this class
    @abc.abstractmethod
    def draw(self, surface):
        pass

    # get_rect method must be present in all classes that inherit this class
    @abc.abstractmethod
    def get_rect(self):
        pass
