#플로이드 워셜 알고리즘
#시간복잡도 O(N3)
INF=int(1e9)

n=int(input())
m=int(input())
#2차원 배열 리스트 만들고 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#(a,a)=0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("lINFINITY", end=' ')
        else:
            print(graph[a][b],end=' ')
    print()