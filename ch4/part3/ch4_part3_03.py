#전체 스테이지의 개수: 200,000: NlogN 으로 충분함
#실패율 = 스테이지에 도달했지만 아직 클리어하지 못한 플레이어/스테이지에 도달한 플레이어의수
#즉 해당 스테이지에 사람이 없으면 그 실패율은 0이란말임

def solution(N,stages):
    answer=[]

    length=len(stages)

    for i in range(1,N+1):
        count=stages.count(i)

        if length==0:
            fail=0
        else:
            fail=count/length

        answer.append((i,fail))
        length-=count
    answer=sorted(answer,key=lambda x:x[1],reverse=True)

    answer=[i[0] for i in answer]

    return answer

