from collections import deque

N = int(input())

def popB(x):
    
    while(x):
        start = x.popleft()
        print(start[0],end=" ")
        if not x:
            break
        if start[1] > 0:
            for i in range(start[1] - 1):
                if x: 
                    a = x.popleft()
                    x.append(a)
        else:
            a = start[1]
            a *= -1
            for i in range(a):
                x.appendleft(x.pop())
                

l = list(map(int,input().split()))
q = deque((i + 1, num) for i, num in enumerate(l))
popB(q)