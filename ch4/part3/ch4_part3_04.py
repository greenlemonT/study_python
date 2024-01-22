#우선순위 큐를 사용하자/ 원소를 넣었다 뺴는것만으로도 정렬된 결과를 가ㅕ옴
#매 상황마다 가장 작은 크기의 두 카드 묶음을 꺼내서 이를 합친다
import heapq

n=int(input())
heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0

while len(heap)!=1:
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)
    sum=one+two
    result+=sum
    heapq.heappush(heap,sum)

print(result)
