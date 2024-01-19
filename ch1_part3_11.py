n=int(input())
k=int(input())
data=[[0]*(n+1) for _ in range(n+1)]
#방향회전 정보
info=[]

for _ in range(k):
    a,b=map(int,input().split())
    data[a][b]=1

l=int(input())
for _ in range(l):
    x,c=input().split()
    info.append((int(x),c))

#처음에는 동쪽보고있으니까 동,남,서,북
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction

def simulate():
    x,y=1,1 #뱀의 머리위치
    data[x][y]=2
    direction=0
    time=0
    index=0 #다음에 회전할 정보
    q=[(x,y)] #뱀이 차지하고있는 칸 정보
    while(1):
        nx=x+dx[direction]
        ny=y+dy[direction]
        #맵안 + 뱀의 몸통 없는위치여야함
        if nx>=1 and nx<=n and ny>=1 and ny<=n and data[nx][ny]!=2:
            #사과없으면 이동후 꼬리제거
            if data[nx][ny]==0:
                data[nx][ny]=2
                q.append((nx,ny))
                px,py=q.pop(0)
                data[px][py]=0
            #사과 있으면 이동만함
            if data[nx][ny]==1:
                data[nx][ny]=2
                q.append((nx,ny))
        else:
            #게임 종결조건
            time+=1
            break
        x,y=nx,ny #다음위치로 머리이동
        time+=1
        if index<1 and time==info[index][0]:
            direction=turn(direction,info[index][1])
            index+=1
    return time

print(simulate())



