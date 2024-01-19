from itertools import permutations

#완전 탐색가능한 경우의 수 / 8!=40320
def solution(n,weak,dist):
    #길이를 2배 늘려서 '원형'을 일자형태로 변형
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    #투입할 친구의 최솟값을 찾아야하므로 +1 한걸로 초기화
    answer=len(dist)+1

    for start in range(length):
        for friends in list(permutations(dist,len(dist))):
            count=1
            position=weak[start]+friends[count-1]
            for index in range(start,start+length):
                if position<weak[index]:
                    count+=1
                    if count>len(dist):
                        break
                    position=weak[index]+friends[count-1]
            answer=min(answer,count)

    if answer>len(dist):
        return -1
    return answer

