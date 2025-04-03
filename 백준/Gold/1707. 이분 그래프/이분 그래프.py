import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(n, one):
    visited[n] = one
    for i in graph[n]:
        if visited[i] == 0:
            if dfs(i, -one):
                pass
            else:
                return False
        elif visited[i] == visited[n]:
            return False

    return True


K = int(input())

for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    Ebun = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            Ebun = dfs(i, 1)
            if Ebun == False:
                break
    if Ebun == True:
        print("YES")
    else:
        print("NO")
