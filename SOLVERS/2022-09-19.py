def collatz(n):
    k = n
    while k != 1:
        if k % 2:
            k = 3*k+1
        else:
            k = k/2
        if k % n == 0:
            return n, k;
    return -1, -1

exc = []
for i in range(1, 10000000+1):
    print(i, ": ", sep="", end="")
    a, b = collatz(i)
    if a != -1: 
        exc.append((a,b))
        print(a, b)
    else: print("Nope")

print(exc)