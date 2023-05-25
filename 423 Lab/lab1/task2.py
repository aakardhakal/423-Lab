from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_point(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()

def drawtriangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.5, 0.5)
    glVertex2f(150, 450)
    glVertex2f(600, 450)
    glVertex2f(380, 650)
    glEnd()

def draw_house():
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_LINES)
    glColor3f(1.0, 0.5, 0.5)
    glVertex2f(150, 50)
    glVertex2f(600, 50)  
    glVertex2f(150, 50)
    glVertex2f(150, 450)
    glVertex2f(150, 450)
    glVertex2f(600, 450)
    glVertex2f(600, 450)
    glVertex2f(600, 50)
    glEnd()

def draw_window():
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(200, 300)
    glVertex2f(300, 300)  
    glVertex2f(300, 400)
    glVertex2f(200, 400)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(450, 300)
    glVertex2f(550, 300)  
    glVertex2f(550, 400)
    glVertex2f(450, 400)
    glEnd()

def draw_door():
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(300, 50)
    glVertex2f(300, 250)  
    glVertex2f(300, 250)
    glVertex2f(450, 250)
    glVertex2f(450, 250)
    glVertex2f(450, 50)
    glEnd()

def iterate():
    glViewport(0, 0, 750, 750)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 750, 0.0, 750, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 0.0, 1.0)  # konokichur color set (RGB)
    #call the draw methods here
    draw_point(430, 150) #door knob
    drawtriangle()
    draw_house()
    draw_window()
    draw_door()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(750, 750)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 01")  # window name
glutDisplayFunc(showScreen)
glutMainLoop()
