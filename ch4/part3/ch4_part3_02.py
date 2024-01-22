n=int(input())
house=list(map(int,input().split()))

#정렬해서 중앙값에 안테나 세우면 나머지 값들과의 차들의 합이 제일 작다

house.sort()
print(house[(n-1)//2])