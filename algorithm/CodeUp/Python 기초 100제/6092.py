from collections import Counter

n=int(input())
array=list(map(int,input().split()))
counter=Counter(array)
for i in range(1,24):
    print(counter[i],end=' ')