#파라메트릭 서치=최적화 문제를 결정문제로 바꾸어 해결하는 기법
#파라메트릭 서치 = 주로 이진탐색 사용
num,length=map(int,input().split())
array=list(map(int,input().split()))

start=0
end=max(array)

result=0
while(start<=end):
    total=0
    mid=(start+end)//2
    for x in array:
        if x>mid:
            total+= (x-mid)

    if total<length:
        end=mid-1

    elif total==length:
        result=mid
        break

    elif total>length:
        start=mid+1

print(result)