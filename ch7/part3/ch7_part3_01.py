#단순히 정렬된 수열에서 특정한 값을 가지는 원소의 개수를 구하는 문제
#이진탐색 라이브러리 bisest사용가능
#bisect_left: 왼쪽 인덱스 알려줌 bisect_right: 오른쪽 인덱스 알려줌
#특정범위에 속하는 원소의 개수구할때 사용가능

from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
    right_index=bisect_right(array,right_value)
    left_index=bisect_left(array,left_value)
    return right_index-left_index

n,x=map(int,input().split())
array=list(map(int,input().split()))

count=count_by_range(array,x,x)

if count==0:
    print(-1)
else:
    print(count)
