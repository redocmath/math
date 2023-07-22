n = 3
history = []
print(n)
n = int((n+2223)/2)
while n != 3:
    if (n % 2):
        n = int((n+2223)/2)
    else:
        n = int(n/2)
    print(n)