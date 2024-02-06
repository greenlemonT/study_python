#도시의개수가 100이하 -> 플로이드워셜가능
#가장 짧은 간선정보만 저장

INF=int(1e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if c<graph[a][b]:
        graph[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
            if graph[a][b]==INF:
                print(0,end=' ')
            else:
                print(graph[a][b],end=' ')
    print()