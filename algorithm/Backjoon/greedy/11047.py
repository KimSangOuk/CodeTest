n,k=map(int,input().split())

data=list()
for i in range(n):
  data.append(int(input()))

data.reverse()

count=0

for i in data:
  if i <= k:
    count+=k//i
    k%=i