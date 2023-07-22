def prime_generator(n): #https:// stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out

n = int(input("Input Number(N=?) : "))
p = int(input("Input Number(언제까지?) : "))

primes = prime_generator(p)
def is_prime(n) :
    return n in primes

def make(p) :
    solve = []
    for a in range(1, p+1) :
        for b in range(1,p+1) :
            for c in range(1, p+1) :
                if (a**2 + b**2 + c**2 - n*a*b*c)%p == 2022%p :
                    solve.append(a)
    solved = set(solve)
    if len(solved) == p :
        return True
    else :
        return False

maked = []
for i in range (3, p+1) :
    if is_prime(i) == True :
        if make(i) == False :
            maked.append(i)
print(maked)