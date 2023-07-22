n = int(input())
cnts = []
for i in range(n,n+1,2):
    tmp = i
    # print(tmp, end=" ")
    cnt = 0
    # if (tmp % 2): 
    #     tmp = (3*tmp-1)/2
    # else: 
    #     tmp = 3/2*tmp
    while tmp % 4 != 0:
        if (tmp % 2): 
            tmp = (3*tmp-1)/2
        else: 
            tmp = 3/2*tmp
            cnt += 1
            if (cnt > len(cnts)): cnts.append(i)
        print(int(tmp%4), "(", int(tmp), ")", end=" ", sep="")
    # print()
    # print(cnt)

    