from itertools import combinations

n,m=map(int,input().split())
chicken,house=[],[]

for a in range(n):
    data=list(map(int,input().split()))
    for b in range(n):
        if data[b]==1:
            house.append((a,b))
        elif data[b]==2:
            chicken.append((a,b))

candidates=list(combinations(chicken,m))

def get_sum(candidate):
    result=0
    for hx,hy in house:
        #각 집마다 치킨집최소거리 구하기위해 한바퀴씩 돌아야함 + 초기화
        temp= 1e9
        for cx,cy in candidates:
            temp=min(temp,abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

result=1e9
for candidate in candidates:
    result=min(result,get_sum(candidate))