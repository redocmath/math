# Get the smallest-element array whose length is n, all elements are not prime

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

def solve(n):
  idx = 1
  a = []
  while n!=0:
    if (primes.count(idx)):
      idx += 1
      continue
    n -= 1
    a.append(idx)
    idx+=1
  return a

print(solve(int(input())))