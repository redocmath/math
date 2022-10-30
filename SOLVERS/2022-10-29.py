def prime_generator(n): #https:// stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

mx = int(input())
primes = prime_generator(mx)
from math import *
li = []
cnt = 0
for i in range(4, mx+1):
    if i not in primes:
        # print(i, end=" ")
        if (len(li) == cnt): li.append(i-cnt)
        cnt += 1
    else:
        # print()
        cnt = 0

for i in range(len(li)):
    print("(", i+1, ",", log(li[i]), ")", end=", ")

