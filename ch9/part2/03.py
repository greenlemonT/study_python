#N의 범위가 100개로 작다
#플로이셜 가능
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#양방향에 cost 1씩이니까
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

#거쳐갈 노드x와 최종목적지 노드k
x,k=map(int,input().split())
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][k]+graph[k][b])

#판매원은 현재 1번노드에 있음
distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print("-1")
else:
    print(distance)