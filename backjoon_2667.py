n=int(input())
num=[]

#2차원 맵 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    global count

    if x<0 or x>=n or y<0 or y>=n:
        return False

    if graph[x][y]==1:
        count+=1
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

count=0
result=0

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            num.append(count)
            result+=1
            count=0 #새로운 dfs돌기전에 count초기화시켜야함

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])