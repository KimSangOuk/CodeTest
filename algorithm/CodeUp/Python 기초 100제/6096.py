arr=[]

for i in range(0,19):
  tmp_arr=list(map(int,input().split()))
  arr.append(tmp_arr)

n=int(input())
for _ in range(n):
  x,y=map(int,input().split())
  for i in range(0,19):
    if arr[x-1][i]==0:
      arr[x-1][i]=1
    else:
      arr[x-1][i]=0
  for i in range(0,19):
    if arr[i][y-1]==0:
      arr[i][y-1]=1
    else:
      arr[i][y-1]=0

for i in range(0,19):
  for j in range(0,19):
    print(arr[i][j],end=" ")
  print()