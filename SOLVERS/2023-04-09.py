n = 0
for i in range(100):
    for j in range(100):
        for k in range(100):
            for l in range(100):
                if 1000*i+100*j+10*k+l == 2010:
                    n += 1

print(n)