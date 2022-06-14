from itertools import combinations

n,s=map(int,input().split())
data=list(map(int,input().split()))

count=0
for i in range(1,n+1):
  new_list=list(combinations(data,i))

  for j in new_list:
    if sum(j)==s:
      count+=1

print(count)