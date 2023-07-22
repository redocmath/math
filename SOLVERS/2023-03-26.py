alps = [1]
def calc(rng):
    for i in range(rng):
        alps.append(3*alps[len(alps)-1])

def get(n,k):
    alp = alps[k]
    a = int(alp*n+(alp-1)/2)

    res = 0
    while True:
        if a%2: return res
        a /= 2
        res += 1

n, k = input().split(" ")
n = int(n)
k = int(k)
calc(k)

for i in range(1, n+1):
    for j in range(1, k+1):
        print(get(i,j), end=" ")
    print()