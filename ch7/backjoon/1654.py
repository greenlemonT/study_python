n,m=map(int,input().split())

array=[]
for _ in range(n):
    array.append(int(input()))
low=1
high=max(array)

while low<=high:
    mid=(low+high)//2
    count=0
    for i in range(len(array)):
        count+=(array[i]//mid)
    if count>=m:
        low=mid+1
    else:
        high=mid-1

print(high)
