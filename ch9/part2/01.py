#다익스트라 / 시간복잡도 O(NlogN)
#튜플로 우선순위큐 구성시 첫번째 원소로 우선순위큐 구성
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

#노드의 개수, 간선의 개수
n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

#a번 노드에서 b까지의 비용이 c/ 튜플로 저장
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        #현재 노드가 이미 처리된 노드라면 pass
        if distance[now]<dist:
            continue
        #현재 노드와 연결된 다른 노드 확인
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])


