#그래프에서 모든 간선의 비용이 동일할떄는 bfs로 최단거리 찾기가능
#노드의 개수 최대가 300,000 : O(N)으로 하자

from collections import deque
#도시의 개수, 도로의 개수,거리 정보, 출발 도시 번호

n,m,k,x=map(int,input().split())

#2차원 리스트 맵정보 받기
#graph = []
#for i in range (n) :
#   graph .append (list(map(int , input())))

#n+1개의 리스트 선언
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

 #n개의 도시 초기화
distance=[-1]*(n+1)
distance[x]=0

#출발 도시 번호 x가 q에 넣어진 상태로 시작함
# -> q= deque()가 아니라 q=deque([x])
#백준7576 토마토 문제는 좌표로 이동하니까 튜플형태로 리스트에 저장
#얘는 그래프니까 distance[도시번호]가 되는거임

q=deque([x])
while q:
    now=q.popleft()
    for next_node in graph[now]:
        if distance[next_node]==-1:
            distance[next_node]=distance[now]+1
            q.append(next_node)

check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True

if check==False:
    print(-1)

