def Gi(i,n,li):
    a = 2**(i-1) * 3**(n-i)
    tmp = 0
    res1 = []
    res2 = []
    while tmp <= li:
        res1.append(tmp)
        tmp+=a
        if (tmp > li):
            break
        res2.append(tmp)
        tmp+=a
    
    return (res1, res2)
        
from math import *
import turtle as tr

# li = int(input())
# for n in range(1, li+1):
# n = int(input())
# step = 10
# sp = float(input("speed: "))

# bo = [0 for _ in range(step)]

# for i in range(1, n+1):
#     a,b = Gi(i, n, step)
#     # print(a,b)
#     if (len(a) != len(b)): b.append(step)
#     for j in range(len(a)):
#         for k in range(a[j]-1, b[j]-1):
#             bo[k] = 1

# print(bo)

# g = []
# res = 0
# tmp = 0
# for i in range(0, step):
#     tmp += 1
#     if (bo[i]):
#         res+=1
#     else: 
#         if (not res): continue
#         if (len(g) != 0 and g[0] == res):
#             g.append(res)
#             break
#         g.append(res)
#         res = 0

# print(g, tmp)


n=int(input())
step=int(input())

tr.setup(width=2000, height=1000)
t = tr.Turtle()
 
t.penup()
t.radians()
t.speed(0)
t.goto(-700,0)

trm = 1400/(step-1)

for i in range(1, step):
    t.dot()
    t.write(str(i) + "\n/" + str(3**n), font=("Arial", 12))
    t.forward(trm)

t.dot()
t.write(str(step) + "\n/" + str(3**n), font=("Arial", 12))

for i in range(1, n+1):
    a,b = Gi(i, n, step)
    if (len(a) != len(b)): b.append(step)
    for j in range(len(a)):
        t.goto(-700+trm*(a[j]-1), 20+i*20)
        t.pendown()
        t.goto(-700+trm*(b[j]-1), 20+i*20)
        t.penup()

input()
