#시간복잡도 O(logN) 써야함
#재귀, 반복문
# def binary_search(array,start,end):
#     if start>end:
#         return None
#     mid=(start+end)//2
#     if array[mid]==mid:
#         return mid
#     elif array[mid]>mid:
#         binary_search(array,start,mid-1)
#     else:
#         binary_search(array,mid+1,end)

def binary_search(array,start,end):
    while(start<=end):
        mid=(start+end)//2
        if array[mid]==mid:
            return mid
        elif array[mid]>mid:
            end=mid-1
        elif array[mid]<mid:
            start=mid+1
        else:
            return -1

n=int(input())
array=list(map(int,input().split()))

index=binary_search(array,0,n-1)
if index==None:
    print(-1)
else:
    print(index)