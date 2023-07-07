arr=[[0]*19 for _ in range(0,19)]
n=int(input())
for _ in range(0,n):
  x,y=map(int,input().split())
  arr[x-1][y-1]=1

for i in range(0,19):
  for j in range(0,19):
    print(arr[i][j],end=" ")
  print()