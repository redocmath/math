from math import *
import turtle as tr
 
n = int(input("n: "))
sp = float(input("speed: "))
md = int(input("mode: ")) # 1: only red 2: only blue
rng = 400
pure = 1

tr.setup(width=1500, height=1000)
t = tr.Turtle()
 
t.penup()
t.radians()
t.speed(sp)
t.goto(0,0)
conn = [[0 for j in range(n)] for i in range(n)]

def line(beg, end, color):
    if md == 1 and color == 'blue':
        return
    if md == 2 and color == 'red':
        return
    beg += 1
    end += 1
    x1 = (rng-30)*cos(beg*2*pi/n+pi/2-2*pi/n)
    y1 = (rng-30)*sin(beg*2*pi/n+pi/2-2*pi/n)
    x2 = (rng-30)*cos(end*2*pi/n+pi/2-2*pi/n)
    y2 = (rng-30)*sin(end*2*pi/n+pi/2-2*pi/n)
    t.color(color)

    if beg == end: 
        t.goto((rng+30)*cos(beg*2*pi/n+pi/2-2*pi/n),(rng+30)*sin(beg*2*pi/n+pi/2-2*pi/n))
        t.pendown()
        t.circle(10)
        t.penup()
        return

    t.goto(x1+conn[beg-1][end-1]*10*pure,y1+conn[beg-1][end-1]*10*pure)
    t.pendown()

    t.goto(x2+conn[beg-1][end-1]*10*pure,y2+conn[beg-1][end-1]*10*pure)
    if x1 > x2:
        t.seth(pi+atan((y1-y2)/(x1-x2)))
    else:
        t.seth(atan((y1-y2)/(x1-x2)))
    t.stamp()
    t.penup()

for i in range(1, n+1):
    t.goto(rng*cos(i*2*pi/n+pi/2-2*pi/n),rng*sin(i*2*pi/n+pi/2-2*pi/n))
    t.write(i-1, font=["",20,""])

# red: operation even, blue: operation odd -> operation e
for modulo in range(0, n):
    print("----", n, "k+", modulo, "----",sep="")
    if modulo % 2: # odd
        tomod = int(((n+modulo)/2)%n)
        conn[modulo][tomod] += 1
        conn[tomod][modulo] += 1
        line(modulo, tomod, 'red')
        print("3x+1 ->", tomod)

        tomod = (3*modulo+1)%n
        if tomod % 2:
            tomod = int(((n+tomod)/2)%n)
        else:
            tomod = int(tomod/2)
        conn[modulo][tomod] += 1
        conn[tomod][modulo] += 1
        line(modulo, tomod, 'blue')
        print("x/2 ->", tomod)
    if modulo % 2 == 0: # even
        tomod = int(modulo/2)
        conn[modulo][tomod] += 1
        conn[tomod][modulo] += 1
        line(modulo, tomod, 'red')
        print("3x+1 ->", tomod)

        tomod = (3*modulo+1)%n
        if tomod % 2:
            tomod = int(((n+tomod)/2)%n)
        else:
            tomod = int(tomod/2)
        conn[modulo][tomod] += 1
        conn[tomod][modulo] += 1
        line(modulo, tomod, 'blue')
        print("x/2 ->", tomod)

print(conn)
input()