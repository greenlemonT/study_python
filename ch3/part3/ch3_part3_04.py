#균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count=0 #왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

#올바른 괄호 문자열인지 판단
def check_proper(p):
    count=0
    for i in p:
        if i =='(':
            count+=1
        else:
            if count==0: #쌍이 맞지않은 경우에 False반환
                return False
            count-=1
    return True

def solution(p):
    answer=''
    if p=='':
        return answer
    index=balanced_index(p)
    u=p[:index+1]
    v=p[index+1:]
    #올바은 괄호 문자열이면 v함수 수행결과를 붙여 반환
    if check_proper(u):
        answer=u+solution(v)
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1]) #첫번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        answer+="".join(u)
    return answer
