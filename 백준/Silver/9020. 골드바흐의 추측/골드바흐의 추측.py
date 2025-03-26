def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1 

a = 0
b = 0
T = int(input())
for i in range(T):
    a = int(input())
    b = int(a/2)
    c = int(a/2)
    for u in range(b):
        if (prime(b)==1 and prime(c)==1):
            print(b,c)
            break
        else:
            b -= 1
            c += 1
