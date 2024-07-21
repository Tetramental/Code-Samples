import pygame
from drawable import Drawable

# File Name: text.py
# Purpose: Contains the Text class for the simple game
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 22, 2019

class Text(Drawable):
    '''A class determining the attributes and behaviors of a Text object.
    Used as the "score" of the simple game'''

    # initialization method
    def __init__(self, x = 0, y = 0, message = "Score: ", size = 32, color = (0, 0, 0)):
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__typeFont = pygame.font.Font("freesansbold.ttf", size)
        self.__surface = self.__typeFont.render(self.__message, True, self.__color)

    # draws a block on a given surface
    def draw(self, surface):
        location = super().getLocation()
        surface.blit(self.__surface, (location[0] - (self.__surface.get_width() // 2), location[1] - (self.__surface.get_height() // 2)))

    # returns a Pygame Rect object that is the bounding rectangle that fits tightly around an object
    def get_rect(self):
        pass

    # sets and increments the score
    # displays the newly updated score
    def setScore(self, newScore, listOfObjectives):
        self.__message = "Score: " + str(newScore) + "/" + str(len(listOfObjectives))
        self.__surface = self.__typeFont.render(self.__message, True, self.__color)

    # sets the color of the Text object
    def setColor(self, color = (0, 0, 0)):
        self.__color = color
