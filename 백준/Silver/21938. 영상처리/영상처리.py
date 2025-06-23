import sys

sys.setrecursionlimit(10**8)

N, M = map(int,input().split())

graph = []

for _ in range(N):
    tmp = list(map(int,input().split()))
    tmp2 = []
    while(tmp):
        tmp3 = 0
        for _ in range(3):
            a = tmp.pop()
            tmp3 += a
        tmp3 = int(tmp3 / 3)
        tmp2.append(tmp3)
        
    graph.append(tmp2)
    
T = int(input())

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] >= T:
            graph[i][j] = 255
        else:
            graph[i][j] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[False] * M for _ in range(N)]

def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] == 255:
                dfs(nx,ny)
                
count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 255 and visited[i][j] == False:
            dfs(i,j)
            count += 1

print(count)