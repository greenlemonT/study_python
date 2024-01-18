data=input()
result=[]
sum=0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        sum+=int(x)

result.sort()

if sum !=0:
    result.append(str(sum))

#리스트를 문자열로 변환하여 출력
print(''.join(result))