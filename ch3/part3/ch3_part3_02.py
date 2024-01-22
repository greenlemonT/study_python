n,m=map(int,input().split())

#초기맵리스트
data=[]

#벽을 설치한뒤의 맵 리스트
temp=[[0]*m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0

#바이러스가 퍼지는 함수(dfs)
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

#현재 맵에서 안전영역 크기 계산
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

#울타리 설치하면서 바이러스 퍼진후의 매번 안전영역 크기 계산
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result=max(result,get_score())
        return
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1
                
dfs(0)
print(result)
