#완전탐색

#2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n=len(a)
    m=len(a[0])
    result=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]

    return result

#자물쇠의 중간부분이 모두 1인지 확인
def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key,lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    #새로운 자물쇠의 중앙부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]

    #4가지 방향 다 적용해보기
    for rotation in range(4):
        key=rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                #자물쇠에 열쇠를 다시 뺴기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]

    return False

