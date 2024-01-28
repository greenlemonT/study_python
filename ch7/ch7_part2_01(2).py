#특정한 데이터가 존재하는지 검사할때에-> 집합자료형 사용

n=int(input())
#집합(set)
array=set(map(int,input().split()))

m=int(input())
x=list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes',end=' ')
    else:
        print('no',end=' ')