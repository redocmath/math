def prime_generator(n): #https:// stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

primes = prime_generator(10000000)

rng = int(input())

for i in range(0, rng):
    res = 1
    for j in range(i):
        res *= primes[j]
    res += 1

    ky = 0
    for j in range(len(primes)):
        if primes[j] >= res:
            ky = j
            break
    
    if primes[ky]-(res-1) not in primes:
        print(i, primes[ky], res, primes[ky]-(res-1))

