import pygame
from drawable import Drawable

# File Name: line.py
# Purpose: Contains the Line class for the simple game
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 22, 2019

class Line(Drawable):
    '''A class determining the attributes and behaviors of a Line object.
    Considered the "ground" of the simple game'''

    # initialization method
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, color = (0, 0, 0)):
        super().__init__(x1, y1)
        self.__pointEnd = (x2, y2)
        self.__color = color

    # draws a line on a given surface
    def draw(self, surface):
        location = super().getLocation()
        pygame.draw.line(surface, self.__color, (location[0], location[1]), (self.__pointEnd[0], self.__pointEnd[1]), 3)

    # returns a Pygame Rect object that is the bounding rectangle that fits tightly around an object
    def get_rect(self):
        pass

    # returns the starting coordinate (x, y) of the Line object
    def getStartPoint(self):
        location = super().getLocation()
        return location

    # returns the ending coordinate (x, y) of the Line object
    def getEndPoint(self):
        return self.__pointEnd

    # sets the color of the Line object
    def setColor(self, color = (0, 0, 0)):
        self.__color = color
