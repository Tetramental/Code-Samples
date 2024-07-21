import random
import pygame
from drawable import Drawable
from ball import Ball
from block import Block
from block import Rectangle
from text import Text
from line import Line

# File Name: main.py
# Purpose: To create a simple game where the objective is to hit a stack of blocks with a ball and knock all the blocks in the stack
# User ID/Name: lwe26@drexel.edu / Lange Eo
# Date: February 22, 2019

# returns True if two rectangles intersect; False otherwise
def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
        return True
    return False

# returns a list of appended arguments
def appendItems(passedList, *args):
    for items in args:
        passedList.append(items)
    return passedList

# initialization
pygame.init()
windowSizeX = 960
windowSizeY = 540
displaySurface = pygame.display.set_mode((windowSizeX, windowSizeY))
pygame.display.set_caption("Homework 03 Pygame")
fpsClock = pygame.time.Clock()

# declaration and assignment of variables
offWhite = (230, 230, 230)
drawables = []
sky = Rectangle((windowSizeX // 2), (windowSizeY * 0.3), windowSizeX, (windowSizeY * 0.6), offWhite)
ground = Rectangle((windowSizeX // 2), (windowSizeY * 0.8), windowSizeX, (windowSizeY * 0.4), (128, 0, 0))
lineGround = Line(0, ground.getHeight() + (ground.getHeight() / 2), windowSizeX, ground.getHeight() + (ground.getHeight() / 2), (0, 0, 0))
ball = Ball(int(0.25 * ground.getWidth()), int((ground.getHeight() + (ground.getHeight() / 2)) - 11), 10, (58, 190, 255))

listBlocks = []
block1 = Block(int(0.75 * ground.getWidth()), int((ground.getHeight() + (ground.getHeight() / 2)) - 14), 25, (229, 124, 4))
block2 = Block(int(0.75 * ground.getWidth()) - 30, int((ground.getHeight() + (ground.getHeight() / 2)) - 14), 25, (229, 124, 4))
block3 = Block(int(0.75 * ground.getWidth()) + 30, int((ground.getHeight() + (ground.getHeight() / 2)) - 14), 25, (229, 124, 4))
block4 = Block(int(0.75 * ground.getWidth()), int((ground.getHeight() + (ground.getHeight() / 2)) - 14) - 30, 25, (229, 124, 4))
block5 = Block(int(0.75 * ground.getWidth()) - 30, int((ground.getHeight() + (ground.getHeight() / 2)) - 14) - 30, 25, (229, 124, 4))
block6 = Block(int(0.75 * ground.getWidth()) + 30, int((ground.getHeight() + (ground.getHeight() / 2)) - 14) - 30, 25, (229, 124, 4))
block7 = Block(int(0.75 * ground.getWidth()), int((ground.getHeight() + (ground.getHeight() / 2)) - 14) - 60, 25, (229, 124, 4))
block8 = Block(int(0.75 * ground.getWidth()) - 30, int((ground.getHeight() + (ground.getHeight() / 2)) - 14) - 60, 25, (229, 124, 4))
block9 = Block(int(0.75 * ground.getWidth()) + 30, int((ground.getHeight() + (ground.getHeight() / 2)) - 14) - 60, 25, (229, 124, 4))

scoreText = Text(100, 40)
score = 0
winText = Text(windowSizeX // 2, windowSizeY // 2, "You Win!", 72, (123, 13, 30))
winText.setVisibility(False)

# appending instances of objects to respective lists
drawables = appendItems(drawables, sky, ground, lineGround, ball, block1, block2, block3, block4, block5, block6, block7, block8, block9, scoreText, winText)
listBlocks = appendItems(listBlocks, block1, block2, block3, block4, block5, block6, block7, block8, block9)

# physics of ball
xv = 0
yv = 0
dt = 0.1
g = 6.67
r = 0.7
eta = 0.5

# game loop
while(True):

    # display grey background
    displaySurface.fill((128, 128, 128))

    # determining if ball has intersected with blocks
    for block in listBlocks:
        if intersect(ball.get_rect(), block.get_rect()) == True:
            block.setVisibility(False)
            score += 1

    # display current score
    scoreText.setScore(score, listBlocks)

    # win condition
    if score == len(listBlocks):
        winText.setVisibility(True)

    # getting new Ball location and storing into tuple
    newX = ball.getLocation()[0] + (dt * xv)
    newY = ball.getLocation()[1] - (dt * yv)
    newLocationTuple = (newX, newY)
    ball.setLocation(newLocationTuple)

    # checks Ball location; changes x and y velocities
    if ball.getLocation()[1] >= (int((ground.getHeight() + (ground.getHeight() / 2)) - 10)) or ball.getLocation()[1] <= 0:
        yv = -r * yv
        xv = eta * xv
    else:
        yv = yv - g * dt
    
    # register events
    for event in pygame.event.get():

        # if player presses "Esc" or the X button
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_ESCAPE):
            pygame.quit()
            exit()

        # if player presses "R"; reset the ball position
        if (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_r):
            xv = 0
            yv = 0
            ball.setLocation((int(0.25 * ground.getWidth()), int((ground.getHeight() + (ground.getHeight() / 2)) - 11)))

        # if player presses the mouse button
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mousePosButtonDown = pygame.mouse.get_pos()
        # if player releases the mouse button
        elif (event.type == pygame.MOUSEBUTTONUP):
            mousePosButtonUp = pygame.mouse.get_pos()
            xv = mousePosButtonUp[0] - mousePosButtonDown[0]
            yv = -(mousePosButtonUp[1] - mousePosButtonDown[1])
    
    # draws everything that's drawable and visible
    for drawable in drawables:
        if drawable.getVisibility() == True:
            drawable.draw(displaySurface)

    # update the display of the surface
    pygame.display.update()
    fpsClock.tick(30)
