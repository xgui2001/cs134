from turtle import *
from math import sqrt

#*****************************************************************************
#  Global variables:  Some HEX colors
#*****************************************************************************

purple = '#8E44AD'
gold = '#F4D03F'
red = '#f01616'
green = '#09d646'
gray = '#8e918f'
blue = '#4287f5'
orange = '#fa922a'

### BEGIN HELPER FUNCTIONS ###
def drawBar(width, length, color):
    """Draws a single rectangle of side length size and given color
    assuming turtle is initially at one of its endpoints.
    Turtle starts traveling along its width and ends at the same point,
    having drawn its length."""
    down()
    pen(fillcolor = color)
    begin_fill()
    forward(width)
    left(90)
    forward(length)
    left(90)
    forward(width)
    left(90)
    forward(length)
    end_fill()
    up()

def initializeTurtle(w, l):
    """Setups up the window and initializes the turtle
    to be at the bottom left corner of the pattern
    facing east (which is the default direction)."""
    padding = w  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = 2 * (l + w), height = 2 * (l + w) )
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(1) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east
    # Put turtle in bottom left corner of the quilt
    up()
    goto(l/2,-l/2)
    down()

def testDrawVortex(width, length, currColor):
    """Initializes turtle, calls drawVortex and saves figure"""
    # initialize turtle
    initializeTurtle(width, length)
    # call drawVortex
    drawVortex(width, length, currColor)
    # save the figure
    getscreen().getcanvas().postscript(file="drawVortex({}, {}, {}).ps".format(width, length, currColor))


### END HELPER FUNCTIONS ###

#*****************************************************************************
# Task 3: Draw recursive vortex (Non-fruitful recursion)
#*****************************************************************************
def drawVortex(width, length, colorList):
    """Draws a colored vortex as described in Lab 9 Task 3.
    """
    if length < 1:
        pass
    else:
        drawBar(width, length, colorList[0]) #draws the first square
        right(180)
        drawBar(width, length, colorList[0])
        left(90)
        forward(width)
        left(90)
        forward(length)
        right(180)
        drawBar(width, length, colorList[0])
        left(90)
        forward(width)
        left(90)
        forward(length)
        right(180)
        drawBar(width, length, colorList[0])
        left(90)
        forward(length-width)
        newcolorList = colorList[1:] # make a new colorList that has the 2nd element till the last element of the original colorList
        newcolorList.append(colorList[0])# add the 1st color from the original list so that it becomes the last element of the new list
        drawVortex(width, length-2*width, newcolorList) #recursively draws the rest of the vortex
                
    
    
    
    
    

#*****************************************************************************
# Testing code given in if __name__ == '__main__' block below
#*****************************************************************************

if __name__=='__main__':
    """Testing code"""
    # Uncomment these (one at a time) to test your drawVortex function
    #testDrawVortex(50, 100, [purple])
    testDrawVortex(50, 250, [orange, gray])
    #testDrawVortex(50, 500, [red, blue, green])
    #testDrawVortex(5, 500, [red, orange, gold, green, blue, purple, gray])
    exitonclick()
