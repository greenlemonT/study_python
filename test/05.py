#최단거리를 묻는게아니라 여행가능한지 불가능한지 여부판단만하면됨
#합집합연산 사용

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a>b:
        parent[b]=a
    else:
        parent[a]=b

#n=여행지의수,m=여행계획에 속한 도시의수
n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

#데이터 입력받으면서 1이면 union처리
for i in range(n):
    data=list(map(int,input().split()))
    for j in range(n):
        if data[j]==1:
            union_parent(parent,i+1,j+1)

plan=list(map(int,input().split()))
result=True

for i in range(m-1):
    if find_parent(parent,plan[i])!=find_parent(parent,plan[i+1]):
        result=False

if result:
    print('YES')
else:
    print('NO')