from collections import deque

def isVPs(x):
    q = deque()
    
    for i in x:
        if i == "(":
            q.append(i)
        else:
            if not q:
                return False
            q.pop()
    if q:
        return False
    else:
        return True

N = int(input())
for i in range(N):
    word = input()
    if isVPs(word):
        print("YES")
    else:
        print("NO")