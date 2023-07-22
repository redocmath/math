tmp = int(input())
cnt = int(input())
for i in range(cnt):
    if (tmp % 2): 
        print("o", end="")
        tmp = (3*tmp-1)/2
    else: 
        print("e", end="")
        tmp = 3/2*tmp
    # print()
    # print(cnt)

    