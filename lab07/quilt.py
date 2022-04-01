from turtle import *

#************************************************************************************
#  Global variables:  Williams colors!
#************************************************************************************

purple = '#8E44AD'
gold = '#F4D03F'

### BEGIN HELPER FUNCTIONS ###
def drawSquare(size, color):
    """Draws a single square of side length size and given color
    assuming turtle is initially at one of its endpoints"""
    down()
    pen(fillcolor = color)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()
    up()

def initializeTurtle(size):
    """Setups up the window and initializes the turtle
    to be at the bottom left corner of the pattern
    facing east (which is the default direction)."""
    padding = 25  # increase if patterns gets cut off
    # Create a turtle window
    setup(width = size + padding, height = size + padding)
    reset() # Clear any existing turtle drawings
            # and reset turtle position & heading.
    pensize(1) # Choose a pen thickness
    speed(0) # Set the speed; 0=fastest, 1=slowest, 6=normal
    # By default turtle starts at (0,0): center of the screen
    # and by default faces east
    # Put turtle in bottom left corner of the quilt
    up()
    goto(-size/2,-size/2)
    down()

def testDrawQuilt(size, level, color1 = purple, color2 = gold):
    """Initializes turtle, calls drawQuilt and saves figure"""
    # initialize turtle
    initializeTurtle(size)
    # call drawQuilt
    drawQuilt(size, level, color1, color2)
    # save the figure
    getscreen().getcanvas().postscript(file="drawQuilt({},{}).ps".format(size, level))


### END HELPER FUNCTIONS ###

#************************************************************************************
# Task 5: Draw recursive quilt (Non-fruitful recursion)
#************************************************************************************

def drawQuilt(size, level, color1 = purple, color2 = gold):
    """Draws a colored quilt as described in Lab 9 Task 3.
    Assume that the turtle is positioned at the bottom left
    end point of quilt facing east before this function is called."""
    if level < 1:
        pass
    if level == 1:
        drawSquare(size, color1)
    else:
        drawSquare(size, color1)
        forward(size/2)
        drawSquare(size/2, color2)
        left(90)
        forward(size/2)
        left(90)
        forward(size/2)
        right(180)
        drawSquare(size/2, color1)
        colorList = color1, color2
        color = (c for c in colorList)
        drawQuilt(size/2, level-1, next(color))
        
        

#************************************************************************************
# Testing code given in if __name__ == '__main__' block below
#************************************************************************************

if __name__=='__main__':
    """Testing code"""
    # Uncomment these (one at a time) to test your drawQuilt function
    #testDrawQuilt(500, 0) # nothing is drawn
    #testDrawQuilt(500, 1)
    #testDrawQuilt(500, 2)
    #testDrawQuilt(500, 3)
    testDrawQuilt(500, 4)
    #testDrawQuilt(500, 5)
    #testDrawQuilt(500, 6)

    # uncomment line below if you don't want turtle screen to close automatically
    exitonclick()
