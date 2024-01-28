#bfs문제네
#낮은번호의 바이러스가 먼저 증식하므로 정렬 후에 큐에 삽입
from collections import deque

n,k=map(int,input().split())

graph=[]
data=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))


data.sort()
q=deque(data)

time,target_x,target_y=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while q:
    virus,s,x,y= q.popleft()
    if s== time:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))

#graph배열은 0부터시작이지만 좌표는 1부터 시작이므로 1뺴줘야지
print(graph[target_x-1][target_y-1])

