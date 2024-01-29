n,m=map(int,input().split())
data=list(map(int,input().split()))

start=1
end=max(data)
value=0
while(start<=end):
    result=0
    mid=(start+end)//2
    for i in data:
        if i>mid:
            result+=(i-mid)
    if result>=m:
        value=mid
        start=mid+1
    else:
        end=mid-1

print(value)