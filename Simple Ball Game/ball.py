import pygame
from drawable import Drawable

# File Name: ball.py
# Purpose: Contains the Ball class for the simple game
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 22, 2019

class Ball(Drawable):
    '''A class determining the attributes and behaviors of a Ball object.
    Considered the player of the simple game'''
    
    # initalization method
    def __init__(self, x = 0, y = 0, radius = 1, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color

    # draws a ball on a given surface
    def draw(self, surface):
        location = super().getLocation()
        pygame.draw.circle(surface, self.__color, (int(location[0]), int(location[1])), self.__radius)

    # returns a Pygame Rect object that is the bounding rectangle that fits tightly around an object
    def get_rect(self):
        location = super().getLocation()
        return pygame.Rect([location[0] - self.__radius, location[1] - self.__radius, self.__radius * 2, self.__radius * 2])

    # returns the radius of the Ball object
    def getRadius(self):
        return self.__radius

    # sets the color of the Ball object
    def setColor(self, color = (0, 0, 0)):
        self.__color = color
