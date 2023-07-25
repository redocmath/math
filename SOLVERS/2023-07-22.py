CLOCKWISE = 1
COUNTERCLOCKWISE = -1

import turtle as tr
import math as m

T = 0
c = 6
epsilon = 0.001
scale = 50

class SOFA:
    # default variable setting
    init = (0, 0)
    rotation = CLOCKWISE
    P = [(0-init[0],-1-init[1]), (c-init[0],-1-init[1]), (c-init[0],-1-c-init[1]), (c+2-init[0],-1-c-init[1]), (c+2-init[0],1-init[1]), (0-init[0],1-init[1])]

    def __init__(self):
        pass

    def Px(self, t):
        pass

    def Py(self, t):
        pass

    def R(self, t):
        if (T < 1):
            return 0
        elif (T <= 2):
            return m.pi/2*(t-1)
        else:
            return m.pi/2

class Hammersley(SOFA):
    init = (0, -1)
    P = [(0-init[0],-1-init[1]), (c-init[0],-1-init[1]), (c-init[0],-1-c-init[1]), (c+2-init[0],-1-c-init[1]), (c+2-init[0],1-init[1]), (0-init[0],1-init[1])]

    def Px(self, t):
        if (t <= 1):
            return (c-4/m.pi)*t
        elif (t < 2):
            return c-4/m.pi*m.cos(m.pi/2*(t-1))
        else:
            return c

    def Py(self, t):
        if (t < 1):
            return -1
        elif (t < 2):
            return -1-4/m.pi*m.sin(m.pi/2*(t-1))
        else:
            return -1*(c-4/m.pi)*(t-2)-1-4/m.pi

class RHAM(SOFA):
    rotation = COUNTERCLOCKWISE

    def Px(self, t):
        if (t <= 1):
            return (c+1)*t
        else:
            return c+1

    def Py(self, t):
        if (t < 2):
            return 0
        else:
            return -(c+1)*(t-2)

tr.setup(width=1500, height=1000)
t = tr.Turtle(shape='circle')
t.shapesize(0.1, 0.1)
t.stamp()
t.hideturtle()
t.speed(0)
t.width(2)

s = tr.Screen()
s.tracer(0)
color = ['red', 'green', 'blue', 'black']


def draw(sofa):
    t.penup()
    t.goto(sofa.Px(T)*scale*3-500, sofa.Py(T)*scale*3+500)
    t.dot(3)
    t.goto(0,0)
    t.dot(3)
    for i in range(2):
        t.penup()
        t.goto(sofa.P[3*i+0][0]*scale, sofa.P[3*i+0][1]*scale)
        t.color(color[2*i+0])
        t.pendown()
        t.goto(sofa.P[3*i+1][0]*scale, sofa.P[3*i+1][1]*scale)
        t.color(color[2*i+1])
        t.goto(sofa.P[3*i+2][0]*scale, sofa.P[3*i+2][1]*scale)

def drawpoints(sofa):
    for i in range(2):
        t.penup()
        t.goto(sofa.P[3*i+0][0]*scale, sofa.P[3*i+0][1]*scale)
        t.dot(3)
        t.goto(sofa.P[3*i+1][0]*scale, sofa.P[3*i+1][1]*scale)
        t.dot(3)
        t.goto(sofa.P[3*i+2][0]*scale, sofa.P[3*i+2][1]*scale)
        t.dot(3)

def update(sofa):
    for i in range(6):
        dPx = (sofa.Px(T)-sofa.Px(T-epsilon))/epsilon
        dPy = (sofa.Py(T)-sofa.Py(T-epsilon))/epsilon
        dR = (sofa.R(T)-sofa.R(T-epsilon))/epsilon
        
        dx = -dPx * m.cos(sofa.R(T)) + (dPy * m.sin(sofa.R(T)) - dR * sofa.P[i][1]) * sofa.rotation
        dy = -dPy * m.cos(sofa.R(T)) + (-1 * dPx * m.sin(sofa.R(T)) + dR * sofa.P[i][0]) * sofa.rotation
        sofa.P[i] = (sofa.P[i][0] + dx*epsilon, sofa.P[i][1] + dy*epsilon)

sofa = RHAM()
draw(sofa)
T += epsilon
while T <= 3:
    update(sofa)
    draw(sofa)
    T += epsilon

s.update()
tr.done()