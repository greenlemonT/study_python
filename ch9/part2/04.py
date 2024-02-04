#n,m 충분히 크니까 다익스트라 사용해야함
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m,start=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def sol(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        #현재노드와 연결된 다른 노드를 하나씩 꺼내보자
        for i in graph[now]:
            cost=dist+i[1]
            #현재노드를 거쳐서 다른 노드로 가는거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

sol(start)

count=0
max_dis=0
for d in distance:
    if d != INF:
        count+=1
        max_dis=max(max_dis,d)

#시작노드는 제외해야하므로 -1
print(count-1,max_dis)


