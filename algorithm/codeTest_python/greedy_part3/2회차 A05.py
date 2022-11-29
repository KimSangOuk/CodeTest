import sys
input=sys.stdin.readline()

n,m=map(int,input().split())
array=list(map(int,input().split()))

array.sort()

count=[0]*(m+1)
for i in array:
  count[i]+=1

result=0

for i in range(1,m+1):
  n-=count[i]
  result+=n*count[i]

print(result)