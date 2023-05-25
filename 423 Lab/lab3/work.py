from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_pixels(x, y):
    glPointSize(2) 
    glBegin(GL_POINTS)
    glVertex2f(x, y) 
    glEnd()

def circle_pixes(x, y, x0, y0):
    draw_pixels(x + x0, y + y0)  # zone 1
    draw_pixels(y + y0, x + x0)  # zone 0
    draw_pixels(-x + x0, y + y0)  # zone 2
    draw_pixels(-y + y0, x + x0)  # zone 3
    draw_pixels(-y + y0, -x + x0)  # zone 4
    draw_pixels(-x + x0, -y + y0)  # zone 5
    draw_pixels(x + x0, -y + y0)  # zone 6
    draw_pixels(y + y0, -x + x0)  # zone 7

def midpoint_circle(radius, x0, y0):
    d = 1 - radius # initial value of d
    x = 0
    y = radius

    circle_pixes(x, y, x0, y0)
    while (x < y):
        # choose East
        if (d < 0):
            d = d + 2*x + 3
            x += 1
        else:
            # choose South East
            d = d + 2*x - 2*y + 5
            x +=1 
            y -=1 

        circle_pixes(x, y, x0, y0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(1.0, 1.0, 0.0)
    x, y, radius = 250, 250, 225 # center and radius of the outer circle
    midpoint_circle(radius, x, y) # outer circle

    glColor3f(0.0, 1.0, 0.0)
    midpoint_circle(radius/2, x+radius/2, y) # right
    midpoint_circle(radius/2, x-radius/2, y) # left
    midpoint_circle(radius/2, x, y+radius/2) # top
    midpoint_circle(radius/2, x, y-radius/2) # bottom

    glColor3f(0.0, 0.0, 1.0)
    midpoint_circle(radius/2, x + math.sin(math.radians(45)) * radius /2, y + math.sin(math.radians(45)) * radius/2) # top right diagonal 
    midpoint_circle(radius/2, x - math.sin(math.radians(45)) * radius /2, y + math.sin(math.radians(45)) * radius/2) # top left diagonal 
    midpoint_circle(radius/2, x - math.sin(math.radians(45)) * radius /2, y - math.sin(math.radians(45)) * radius/2) # bottom left diagonal 
    midpoint_circle(radius/2, x + math.sin(math.radians(45)) * radius /2, y - math.sin(math.radians(45)) * radius/2) # bottom right diagonal 

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 03")  # window name
glutDisplayFunc(showScreen)
glutMainLoop()
