from itertools import combinations
import time

n,m=map(int,input().split())
data=list(map(int,input().split()))

start=time.time()

count=0

c=len(list(combinations(data,2)))

data.sort()
for i in range(0,len(data)-1):
  if data[i]==data[i+1]:
    count+=1

result=c-count
print(result)

end=time.time()
print(end-start)