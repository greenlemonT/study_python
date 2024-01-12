n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) #양방향이니까
visited=[0]*(n+1)
count=-1 #시작노드는 count에 안세니까

def dfs(v):
    visited[v]=1
    global count
    count+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(count)

