#0으로 바꿨을때와 1로 다 바꿨을때 둘중 더 작은것으로 골라야함
#숫자가 바뀌는 것을 기준으로 +1씩 더해짐


data=input()
count0=0  #전부 0으로 바꾸는경우
count1=0  #전부 1으로 바꾸는경우

if data[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1]=='0':
            count1+=1
        else:
            count0+=1

print(min(count0,count1))