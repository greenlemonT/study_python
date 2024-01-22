#deque사용하는 예제 / list보다 deque가 빠르다
from collections import deque

m,n=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
q=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            q.append([i,j])

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                q.append([nx,ny])
bfs()
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    count=max(count,max(i))

#처음 시작이 1로 시작했으니 1을 빼줘야지
print(count-1)