cnt = 0
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if (c == d): continue
                if (10*d-c)*(10*a+b)==99*d*c: 
                    cnt += 1
                    print(a,b,c,d)

print(cnt)
