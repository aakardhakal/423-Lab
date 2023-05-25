from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_digits():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES)
    
    # 2
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(10,300)
    glVertex2f(60,300)
    glVertex2f(60, 300)
    glVertex2f(60, 250)
    glVertex2f(60, 250)
    glVertex2f(10, 250)
    glVertex2f(10, 250)
    glVertex2f(10, 200)
    glVertex2f(10, 200)
    glVertex2f(60, 200)

    # 0
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(70, 200)
    glVertex2f(120, 200)
    glVertex2f(120, 200)
    glVertex2f(120, 300)
    glVertex2f(120, 300)
    glVertex2f(70, 300)
    glVertex2f(70, 300)
    glVertex2f(70, 200)

    # 2
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(130,300)
    glVertex2f(180,300)
    glVertex2f(180, 300)
    glVertex2f(180, 250)
    glVertex2f(180, 250)
    glVertex2f(130, 250)
    glVertex2f(130, 250)
    glVertex2f(130, 200)
    glVertex2f(130, 200)
    glVertex2f(180, 200)

    # 0
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(190, 200)
    glVertex2f(240, 200)
    glVertex2f(240, 200)
    glVertex2f(240, 300)
    glVertex2f(240, 300)
    glVertex2f(190, 300)
    glVertex2f(190, 300)
    glVertex2f(190, 200)

    # 1
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(250, 200)
    glVertex2f(300, 200)
    glVertex2f(275, 200)
    glVertex2f(275, 300)
    glVertex2f(275, 300)
    glVertex2f(250, 275)


    # 2
    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(310,300)
    glVertex2f(360,300)
    glVertex2f(360, 300)
    glVertex2f(360, 250)
    glVertex2f(360, 250)
    glVertex2f(310, 250)
    glVertex2f(310, 250)
    glVertex2f(310, 200)
    glVertex2f(310, 200)
    glVertex2f(360, 200)

    # 0
    glColor3f(1.0, 0.5, 0.0)
    glVertex2f(370, 200)
    glVertex2f(420, 200)
    glVertex2f(420, 200)
    glVertex2f(420, 300)
    glVertex2f(420, 300)
    glVertex2f(370, 300)
    glVertex2f(370, 300)
    glVertex2f(370, 200)

    # 3
    glColor3f(0.0, 0.9, 1.0)
    glVertex2f(430, 200)
    glVertex2f(480, 200)
    glVertex2f(480, 200)
    glVertex2f(480, 300)
    glVertex2f(480, 300)
    glVertex2f(430, 300)
    glVertex2f(480, 250)
    glVertex2f(430, 250)

    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #konokichur color set (RGB)
    draw_digits()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 01") #window name
glutDisplayFunc(showScreen)
glutMainLoop()
