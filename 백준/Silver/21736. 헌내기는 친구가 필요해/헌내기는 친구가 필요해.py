import sys

sys.setrecursionlimit(10 ** 8)

N, M = map(int,input().split()) 

visited = [[False] * M for _ in range(N)]
graph = []
count = 0

for _ in range(N):
    a = input()
    graph.append(a)
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    global count
    visited[x][y] = True
    if graph[x][y] == "P":
        count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != "X" and not visited[nx][ny]:
            dfs(nx,ny)
            
for i in range(N):
    for e in range(M):
        if not visited[i][e] and graph[i][e] == "I":
            dfs(i,e)

if count > 0:
    print(count)
else:
    print("TT")