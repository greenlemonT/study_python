a,b=map(int,input().split())
data=list(map(int,input().split()))

array=[0]*11 #1부터 10까지 무게 담기
for x in data:
    array[x]+=1

result=0
for i in range(1,b+1):
    a -=array[i] #자기무게인 공 갯수 제외
    result+=array[i]*a

print(result)
