import pygame
from drawable import Drawable

# File Name: block.py
# Purpose: Contains the Block and Rectangle classes for the simple game
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 22, 2019

class Block(Drawable):
    '''A class determining the attributes and behaviors of a Block object.
    Considered the "objectives" of the simple game'''

    # initialization method
    def __init__(self, x = 0, y = 0, side = 1, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__side = side
        self.__color = color

    # draws a block on a given surface
    def draw(self, surface):
        location = super().getLocation()
        pygame.draw.rect(surface, self.__color, ((location[0] - (self.__side // 2)), (location[1] - (self.__side // 2)), self.__side, self.__side))

    # returns a Pygame Rect object that is the bounding rectangle that fits tightly around an object
    def get_rect(self):
        location = super().getLocation()
        if super().getVisibility() == True:
            return pygame.Rect([location[0] - (self.__side // 2), location[1] - (self.__side // 2), self.__side, self.__side])
        else:
            return pygame.Rect([0, 0, 0, 0])

    # returns the side of the Block object
    def getSide(self):
        return self.__side

    # sets the color of the Block object
    def setColor(self, color = (0, 0, 0)):
        self.__color = color

class Rectangle(Drawable):
    '''A class determining the attributes and behaviors of a Rectangle object.
    Considered the "environment" of the simple game'''

    # initalization method
    def __init__(self, x = 0, y = 0, width = 1, height = 1, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    # draws a rectangle
    def draw(self, surface):
        location = super().getLocation()
        pygame.draw.rect(surface, self.__color, ((location[0] - (self.__width // 2)), (location[1] - (self.__height // 2)), self.__width, self.__height))

    # returns a Pygame Rect object that is the bounding rectangle that fits tightly around an object
    def get_rect(self):
        pass
    
    # returns the width of the Rectangle object
    def getWidth(self):
        return self.__width

    # returns the height of the Rectangle object
    def getHeight(self):
        return self.__height

    # sets the color of the Rectangle object
    def setColor(self, color = (0, 0, 0)):
        self.__color = color
