a=int(input())
num=list(map(int,input().split()))
num.sort()

target=1
for i in num:
    if target<i:
        break
    target+=i

print(target)