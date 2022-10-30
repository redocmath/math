n = int(input())
for i in range(1,n+1):
    tmp = i
    print(tmp, end=" ")
    while tmp % 4 != 1:
        if (tmp % 2): tmp = (3*tmp-1)/2
        else: tmp = 3/2*tmp
        print(int(tmp%4), end=" ")
    print()
    