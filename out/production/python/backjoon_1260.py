from collections import deque
N,M,V= map(int,input().split())

graph=[[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

visited1=[0]*(N+1) #dfs
visited2=[0]*(N+1) #bfs

def dfs(V):
    visited1[V]=1
    print(V,end="")
    for i in range(1,N+1):
        if not visited1[i] and graph[V][i]:
            dfs(i)

def bfs(V):
    q=deque([V])
    visited2[V]=1
    while q:
        V=q.popleft()
        print(V,end="")
        for i in range(1,N+1):
            if not visited2[i] and graph[V][i]:
                q.append(i)
                visited2[i]=1

dfs(V)
print()
bfs(V)