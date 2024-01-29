import sys
from collections import Counter

m=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

c=Counter(a)

for i in b:
    if i in c:
        print(c[i],end=' ')
    else:
        print(0,end=' ')