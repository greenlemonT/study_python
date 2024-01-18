def solution(s):
    answer=len(s)
    for step in range(1,len(s)//2+1):
        compressed=""
        prev=s[0:step]
        count=1
        for j in range(step,len(s),step):

            if prev==s[j:j+step]:
                count+=1

            else:
                if count>=2:
                    compressed+=str(count)+prev
                else:
                    compressed=prev

        #남아있는 문자열에 대한 처리
        if count>=2:
            compressed+=str(count)+prev
        else:
            compressed=prev
        answer=min(answer,len(compressed))

    return answer
