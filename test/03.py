#LIS알고리즘 -> DP / 이분탐색
n=int(input())
array=list(map(int,input().split()))
#역으로 배치해서 내림차순되도록
array.reverse()
dp=[1]*n

# #i = 자기자신 , j= 자기자신의앞에있는것
# for i in range(1,n):
#     for j in range(0,i):
#         if array[j]<array[i]:
#             dp[i]=max(dp[i],dp[j]+1)
#
# print(n-max(dp))

#난 이게 더 직관적인듯
for i in range(1,n):
    for j in range(i):
        if array[j]<array[i] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

print(n-max(dp))
