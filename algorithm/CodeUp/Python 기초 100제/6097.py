h, w = map(int,input().split())

arr=[[0]*w for _ in range(0,h)]
n=int(input())

for _ in range(n):
  i,d,x,y=map(int,input().split())
  if d==0: #세로
    for k in range(0,i):
      arr[(x-1)][(y-1)+k]=1
  else: #가로
    for k in range(0,i):
      arr[(x-1)+k][(y-1)]=1

for i in range(0,h):
  for j in range(0,w):
    print(arr[i][j],end=" ")
  print()