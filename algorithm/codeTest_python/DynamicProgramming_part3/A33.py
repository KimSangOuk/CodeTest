import sys

n = int(sys.stdin.readline())

array=[[0]*2 for _ in range(n+1)]

d=[0]*(n+1)
time=[[] for i in range(n+1)]

for i in range(1,n+1):
  a,b=map(int,sys.stdin.readline().split())
  array[i][0]=a
  array[i][1]=b

for i in range(1,n+1):
  if i+array[i][0]-1<=n:
    # print(i+array[i][0]-1)
    time[i+array[i][0]-1].append(array[i])

# for i in range(n+1):
  # print(time[i])

for i in range(1,n+1):
  largest=max(0,d[i-1])
  for j in range(len(time[i])):
    largest=max(largest,d[i-time[i][j][0]]+time[i][j][1])
  if largest>0:
    d[i]=largest
  else:
    d[i]=d[i-1]



# for i in range(n+1):
  # print(d[i])
print(d[n])